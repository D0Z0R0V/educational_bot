from aiogram.filters.callback_data import CallbackData
from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


class Pagination(CallbackData, prefix="pag"):
    class_name: str
    action: str
    page: int

def paginator(class_name: str, page: int = 0):
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(text="⏪", callback_data=Pagination(action="prev", class_name=class_name, page=page).pack()),
        InlineKeyboardButton(text="⏩", callback_data=Pagination(action="next", class_name=class_name, page=page).pack()),
        width=2
    )
    return builder.as_markup()