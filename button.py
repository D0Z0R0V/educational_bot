import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import *
from func import *

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: CallbackContext):
    keyboard = [
        [
            InlineKeyboardButton("7 класс", callback_data='7_class'),
            InlineKeyboardButton("9 класс", callback_data='9_class'),
            InlineKeyboardButton("10 класс", callback_data='10_class')
        ],
        [
            InlineKeyboardButton("Приложения", callback_data='apps')
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Выберите класс:",
        reply_markup=reply_markup
    )

async def button(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    if query.data == '7_class':
        await show_7_class_menu(query)
    elif query.data == '9_class':
        await show_9_class_menu(query)
    elif query.data == '10_class':
        await show_10_class_menu(query)
    elif query.data == 'apps':
        await show_apps_menu(query)
    elif query.data == 'back_to_start': 
        await start(update, context)

async def show_7_class_menu(query):
    keyboard = [
        [
            InlineKeyboardButton("Явление тяготения. Сила тяжести.", callback_data='gravity_phenomenon')
        ],
        [    
            InlineKeyboardButton("Сила тяжести на других планетах", callback_data='gravity_force')
        ],
        [
            InlineKeyboardButton("Назад", callback_data='back_to_start') 
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.message.edit_text(
        text="Выберите тему:",
        reply_markup=reply_markup
    )

async def button_7_class(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    if query.data == 'gravity_phenomenon':
        await query.message.edit_text(text="Теоретический материал по явлению тяготения")
    elif query.data == 'gravity_force':
        await query.message.edit_text(text="Теоретический материал по силе тяжести на других планетах")
    elif query.data == 'back_to_start':
        await start(update, context)

async def show_9_class_menu(query):
    keyboard = [
        [
            InlineKeyboardButton("Закон всемирного тяготения", callback_data="universal_gravity")
        ],
        [
            InlineKeyboardButton("Ускорение свободного падения на земле.", callback_data="free_fall")
        ],  
        [    
            InlineKeyboardButton("Искусственные спутники Земли", callback_data="earth_satellites") 
        ],
        [
            InlineKeyboardButton("Назад", callback_data='back_to_start')
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.message.edit_text(
        text="Выберите тему:",
        reply_markup=reply_markup
    )

async def button_9_class(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    if query.data == 'universal_gravity':
        await query.message.edit_text(text="Теоретический материал по закону всемирного тяготения")
    elif query.data == 'free_fall':
        await query.message.edit_text(text='Теоретический материал по ускорению свободного падения')
    elif query.data == 'earth_satellites':
        await query.message.edit_text(text='Теоретический материал по искусственным спутникам Земли')
    elif query.data == 'back_to_start':
        await start(update, context)

async def show_10_class_menu(query):
    keyboard = [
        [
            InlineKeyboardButton("Сила тяжести и сила всемирного тяготения", callback_data="gravity"),
        ],
        [
            InlineKeyboardButton("Сила тяжести на других планетах", callback_data="on_other_planets"),
        ],
        [
            InlineKeyboardButton("Первая космическая скорость", callback_data="space")
        ],
        [
            InlineKeyboardButton("Назад", callback_data='back_to_start')
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.message.edit_text(
        text="Выберите тему:",
        reply_markup=reply_markup
    )

async def button_10_class(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    if query.data == 'gravity':
        await query.message.edit_text(text='Теоретический материал по силе тяжести и силе всемирного тяготения')
    elif query.data == 'on_other_planets':
        await query.message.edit_text(text='Теоретический материал по силе тяжести на других планетах')
    elif query.data == 'space':
        await query.message.edit_text(text='Теоретический материал по первой космической скорости')
    elif query.data == 'back_to_start':
        await start(update, context)

async def show_apps_menu(query):
    keyboard = [
        [
            InlineKeyboardButton("конспект урока", callback_data="lesson_summary")
        ],
        [
            InlineKeyboardButton("тестовые задания", callback_data="test_tasks")
        ],
        [
            InlineKeyboardButton("задачи", callback_data="tasks")
        ],
        [
            InlineKeyboardButton("мультимедийные материалы", callback_data="multimedia_materials")
        ],
        [
            InlineKeyboardButton("историческая справка", callback_data="historical_background")
        ],
        [
            InlineKeyboardButton("словарь", callback_data="dictionary")
        ],
        [
            InlineKeyboardButton("Назад", callback_data='back_to_start')
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.message.edit_text(
        text="Выберите тему:",
        reply_markup=reply_markup
    )

async def button_apps(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    if query.data == "lesson_summary":
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Конспекты уроков")
        await displayLessonSummary(update, context)
    elif query.data == "test_tasks":
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Тестовые задания, чтоб \
            вы смогли закрепить свои знания")
        await displayTestTasks(update, context)
    elif query.data == "tasks":
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Задачи, которые \
            вы можете решить самостоятельно")
        await displayTasks(update, context)
    elif query.data == "multimedia_materials":
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Мультимедийные материалы")
        await displayMultimediaMaterials(update, context)
    elif query.data == "historical_background":
        await context.bot.send_message(chat_id=update.effective_chat, text="Историческая справка по разным темам")
        await displayHistoricalBackground(update, context)
    elif query.data == "dictionary":
        await context.bot.send_message(chat_id=update.effective_chat, text="Словарь")
        await displayDictionary(update, context)
    elif query.data == "back_to_start":
        await start(update, context)        