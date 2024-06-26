from contextlib import suppress
from aiogram import Router, F, types
from aiogram.types import CallbackQuery
from aiogram.exceptions import TelegramBadRequest
from aiogram.enums import ChatAction

from keyboards import fabrics
from data.subloader import get_json_data

router = Router()

@router.callback_query(fabrics.Pagination.filter(F.action.in_(["prev", "next"])))
async def pagination_handler(call: CallbackQuery, callback_data: fabrics.Pagination):
    smiles = await get_json_data(callback_data.file_name)

    if not smiles:
        await call.answer("Данные не найдены", show_alert=True)
        return

    page_num = int(callback_data.page)

    if callback_data.action == "next":
        page_num += 1
        if page_num >= len(smiles):
            page_num = 0  # Если достигли конца, возвращаемся к началу
    elif callback_data.action == "prev":
        page_num -= 1
        if page_num < 0:
            page_num = len(smiles) - 1  # Если достигли начала, переходим к концу

    item = smiles[page_num]
    photo_path = item[0]
    caption = item[1]
    
    print(f"Action: {callback_data.action}, Page: {page_num}, Data: {item}")

    with suppress(TelegramBadRequest):
        if photo_path:
            await call.message.bot.send_chat_action(
                chat_id=call.message.chat.id,
                action=ChatAction.UPLOAD_PHOTO
            )
            photo = types.FSInputFile(photo_path)
            await call.message.answer_photo(
                photo=photo,
                caption=caption,
                reply_markup=fabrics.paginator(page_num, callback_data.file_name)
            )
        else:
            await call.message.bot.send_chat_action(
                chat_id=call.message.chat.id,
                action=ChatAction.TYPING
            )
            await call.message.answer(
                text=caption,
                reply_markup=fabrics.paginator(page_num, callback_data.file_name)
            )
        await call.message.delete()
    await call.answer()