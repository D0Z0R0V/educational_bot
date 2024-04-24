from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)

main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='7 класс'),
                                     KeyboardButton(text='9 класс'),
                                     KeyboardButton(text='10 класс')],
                                     [KeyboardButton(text='Приложения')]],
                           resize_keyboard=True,
                           input_field_placeholder='Выберите подходящий пункт меню...')


class_7 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Явление тяготения. Сила тяжести', callback_data='Gravity')],
    [InlineKeyboardButton(text='Cила тяжести на других планетах', callback_data='planets')]])

class_9 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Закон всемирного тяготения', 
                          callback_data='law')],
    [InlineKeyboardButton(text='Ускорение свободного падения на земле и других небесных телах', 
                          callback_data='boost')],
    [InlineKeyboardButton(text='Искусственные спутники земли', 
                          callback_data='artificial_satellites')]])


class_10 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Сила тяжести и сила всемирного тяготения', callback_data='_universal_gravity')],
    [InlineKeyboardButton(text='Сила тяжести на других планетах', callback_data='other_planets')],
    [InlineKeyboardButton(text='Первая космическая скорость', callback_data='first_speed')]])

apps = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='конспект урока', callback_data='abstract'),
     InlineKeyboardButton(text='тестовые задания', callback_data='test_tasks'),
     InlineKeyboardButton(text='задачи', callback_data='tasks')],
    [InlineKeyboardButton(text='мультимедийные материалы', callback_data='multimedia'),
     InlineKeyboardButton(text='историческая справка', callback_data='history'),
     InlineKeyboardButton(text='словарь', callback_data='dictionary')]])


get_number = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Отправить номер',
                                                           request_contact=True)]],
                                 resize_keyboard=True)