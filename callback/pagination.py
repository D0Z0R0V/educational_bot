from contextlib import suppress
from aiogram import Router, F
from aiogram.types import CallbackQuery, InputFile
from aiogram.exceptions import TelegramBadRequest

from keyboards import fabrics
from data.subloader import get_json_data


router = Router()

@router.callback_query(fabrics.Pagination.filter(F.action.in_(["prev", "next"])))
async def pagination_handler(call: CallbackQuery, callback_data: fabrics.Pagination):
    class_name = callback_data.class_name
    smiles = await get_json_data("class.json")
    
    if class_name not in smiles:
        await call.answer("Invalid class selected", show_alert=True)
        return

    page_num = int(callback_data.page)
    page = page_num - 1 if callback_data.action == "prev" and page_num > 0 else page_num

    if callback_data.action == "next":
        page = page_num + 1 if page_num < (len(smiles[class_name]) - 1) else page_num

    image_path, description = smiles[class_name][page]

    with suppress(TelegramBadRequest):
        await call.message.delete()  # Удалить старое сообщение
        await call.message.answer_photo(
            photo=InputFile(image_path),
            caption=f"<b>{description}</b>",
            reply_markup=fabrics.paginator(class_name, page)
        )
    await call.answer()