from telegram.ext import *
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup

async def displayLessonSummary(update: Update, context: CallbackContext):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Lesson Summary")

async def displayTestTasks(update: Update, context: CallbackContext):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="test_tasks")

async def displayTasks(update: Update, context: CallbackContext):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="tasks")

async def displayMultimediaMaterials(update: Update, context: CallbackContext):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="MultimediaMaterials")

async def displayHistoricalBackground(update: Update, context: CallbackContext):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="historical_background")

async def displayDictionary(update: Update, context: CallbackContext):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Dictionary")