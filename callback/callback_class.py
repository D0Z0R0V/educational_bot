from aiogram import Router, F
from aiogram.types import CallbackQuery

router = Router()

@router.callback_query(F.data == 'Gravity')
async def query_7_class(callback: CallbackQuery):
    await callback.answer('Вы выбрали категорию')
    await callback.message.answer('Вы выбрали тему. В будущем тут появится определенный текст')
    
@router.callback_query(F.data == 'test_7')
async def test_7_class(callback: CallbackQuery):
    await callback.answer('Вы выбрали категорию')
    await callback.message.answer('Вы выбрали тему. В будущем тут появится определенный текст')
    
@router.callback_query(F.data == 'test_9')
async def test_9_class(callback: CallbackQuery):
    await callback.answer('Вы выбрали категорию')
    await callback.message.answer('Вы выбрали тему. В будущем тут появится определенный текст')
    
@router.callback_query(F.data == 'test_10')
async def test_10_class(callback: CallbackQuery):
    await callback.answer('Вы выбрали категорию')
    await callback.message.answer('Вы выбрали тему. В будущем тут появится определенный текст')