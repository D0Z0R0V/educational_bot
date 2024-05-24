from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.types import Message 

from data.subloader import get_json_data
from keyboards import fabrics

router = Router()

@router.callback_query(F.data == "Gravity")
async def get_7_class(callback: CallbackQuery):
    smiles = await get_json_data("class7.json")
    await callback.answer('Вы выбрали категорию')
    await callback.message.answer(text=f"{smiles[0][0]} <b>{smiles[0][1]}</b>", reply_markup=fabrics.paginator())
    
@router.message()
async def get_72_class(message: Message):
    msg = message.text()
    smiles = await get_json_data("class72.json")
    if message.data == 'Planets':
        await message.answer(text=f"{smiles[0][0]} <b>{smiles[0][1]}</b>", reply_markup=fabrics.paginator())
    
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