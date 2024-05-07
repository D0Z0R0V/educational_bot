from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='7 класс'),
                                     KeyboardButton(text='9 класс'),
                                     KeyboardButton(text='10 класс')],
                                     [KeyboardButton(text='Приложения')]],
                           resize_keyboard=True,
                           input_field_placeholder='Выберите подходящий пункт меню...')

get_number = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Отправить номер',
                                                           request_contact=True)]],
                                 resize_keyboard=True)