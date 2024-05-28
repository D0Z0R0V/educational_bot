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
    await callback.message.answer(text=f"{smiles[0][0]} <b>{smiles[0][1]}</b>", reply_markup=fabrics.paginator(file_name="class7.json"))
    
@router.callback_query(F.data == "Planets")
async def get_72_class(callback: CallbackQuery):
    smiles = await get_json_data("class72.json")
    await callback.answer('Вы выбрали категорию')
    await callback.message.answer(text=f"{smiles[0][0]} <b>{smiles[0][1]}</b>", reply_markup=fabrics.paginator(file_name="class72.json"))
    
@router.callback_query(F.data == "law")
async def get_9_class(callback: CallbackQuery):
    smiles = await get_json_data("class9.json")
    await callback.answer('Вы выбрали категорию')
    await callback.message.answer(text=f"{smiles[0][0]} <b>{smiles[0][1]}</b>", reply_markup=fabrics.paginator(file_name="class9.json"))
    
@router.callback_query(F.data == "boost")
async def get_92_class(callback: CallbackQuery):
    smiles = await get_json_data("class92.json")
    await callback.answer('Вы выбрали категорию')
    await callback.message.answer(text=f"{smiles[0][0]} <b>{smiles[0][1]}</b>", reply_markup=fabrics.paginator(file_name="class92.json"))
    
@router.callback_query(F.data == "artificial_satellites")
async def get_93_class(callback: CallbackQuery):
    smiles = await get_json_data("class93.json")
    await callback.answer('Вы выбрали категорию')
    await callback.message.answer(text=f"{smiles[0][0]} <b>{smiles[0][1]}</b>", reply_markup=fabrics.paginator(file_name="class93.json"))