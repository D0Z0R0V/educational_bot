from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

class_7 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Явление тяготения. Сила тяжести', callback_data='Gravity')],
    [InlineKeyboardButton(text='Cила тяжести на других планетах', callback_data='Planets')]])

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

test_class = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Тестовые задания для 7 класса', url='https://onlinetestpad.com/oiupgzlfatas4')],
    [InlineKeyboardButton(text='Тестовые задания для 9 класса', url='https://onlinetestpad.com/5s7nf3zizhvyg')],
    [InlineKeyboardButton(text='Тестовые задания для 10 класса', url='https://onlinetestpad.com/ap4cmnfkwsglc')]])

tasks = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Задачи с решением', callback_data='solution')],
    [InlineKeyboardButton(text='Задачи из ОГЭ',callback_data='task_OGE')],
    [InlineKeyboardButton(text='Задачи из ЕГЭ', callback_data='task_EGE')]])

task_solution = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Уровень А', callback_data='level_A')],
    [InlineKeyboardButton(text='Уровень В', callback_data='level_B')],
    [InlineKeyboardButton(text='Уровень С', callback_data='level_C')]])

multimedia = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Опыт Г.Кавендиша', url='https://disk.yandex.com.am/i/vv9ebDMCXMdFDg')],
    [InlineKeyboardButton(text='Опыт Ф.Жолли', url='https://disk.yandex.com.am/i/r6UM38TQ0F-3VA')],
    [InlineKeyboardButton(text='Gif - первой космической скорости', callback_data='gif')]])

hist_information = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Мультимедийная презентация', url='https://disk.yandex.ru/i/C8K_t8dSSN3Ffw')],
    [InlineKeyboardButton(text='Текстовый документ', url='https://disk.yandex.ru/i/oXJjkJveTXJSDQ')]])

dictionary = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Сила тяжести', callback_data='power'),
     InlineKeyboardButton(text='Гравитационные силы', callback_data='gravitation')],
    [InlineKeyboardButton(text='Всемирное тяготение', callback_data='universal_gravity'),
     InlineKeyboardButton(text='Гравитационная постоянная', callback_data='constant_gr')],
    [InlineKeyboardButton(text='Закон всемирного тяготения', callback_data='law_gravity'),
     InlineKeyboardButton(text='Масса', callback_data='weight')],
    [InlineKeyboardButton(text='Искусственные спутники земли', callback_data='satellites'),
     InlineKeyboardButton(text='Первая космичесая скорость', callback_data='cosmic_velocity')],
    ])