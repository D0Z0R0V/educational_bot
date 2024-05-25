from aiogram.filters.callback_data import CallbackData
from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


class Pagination(CallbackData, prefix="pag"):
    action: str
    page: int
    file_name: str

def paginator(page: int = 0, file_name: str = "um.json"):
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(text="⏪", callback_data=Pagination(action="prev", page=page, file_name=file_name).pack()),
        InlineKeyboardButton(text="⏩", callback_data=Pagination(action="next", page=page, file_name=file_name).pack()),
        width=2
    )
    return builder.as_markup()
