from contextlib import suppress
from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.exceptions import TelegramBadRequest
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
    elif callback_data.action == "prev":
        page_num -= 1

    # Убедитесь, что индекс страницы находится в допустимом диапазоне
    page_num = max(0, min(page_num, len(smiles) - 1))
    
    print(f"Action: {callback_data.action}, Page: {page_num}, Data: {smiles[page_num]}")

    with suppress(TelegramBadRequest):
        await call.message.edit_text(
            f"{smiles[page_num][0]} <b>{smiles[page_num][1]}</b>",
            reply_markup=fabrics.paginator(page_num, callback_data.file_name)
        )
    await call.answer()
