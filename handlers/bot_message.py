from aiogram import F, Router
from aiogram.types import Message
from aiogram.filters import Command, CommandStart

from keyboards import replay, inline


router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer_sticker(sticker='CAACAgIAAxreplayAAEL_bFmK1wHzF7Lm-Kg415zk-5St4Tn-AACYw4AAgtaoEg7Cb-9icYZzTQE')
    await message.answer('Привет!\n Я твой помощник в мире физике, пожалуйста выбери\
        интересующую тебя тему', reply_markup=replay.main)

@router.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer('Вы воспользовались кнопкой помощи')
    
@router.message(F.text == '7 класс')
async def button_7_class(message: Message):
    await message.answer('Выберите нужную тему', reply_markup=inline.class_7)
    
@router.message(F.text == '9 класс')
async def button_9_class(message: Message):
    await message.answer('Выберите нужную тему', reply_markup=inline.class_9)
    
@router.message(F.text == '10 класс')
async def button_10_class(message: Message):
    await message.answer('Выберите нужную тему', reply_markup=inline.class_10)
    
@router.message(F.text == 'Приложения')
async def apps(message: Message):
    await message.answer('Выберите нужную тему', reply_markup=inline.apps)