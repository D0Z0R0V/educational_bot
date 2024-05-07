from aiogram import Router, F
from aiogram.types import CallbackQuery

from keyboards import inline

router = Router()


@router.callback_query(F.data == 'test_tasks')
async def query_7_class(callback: CallbackQuery):
    await callback.answer('Вы выбрали категорию')
    await callback.message.answer('Выберите нужную тему', reply_markup=inline.test_class)
    
@router.callback_query(F.data == 'tasks')
async def task(callback: CallbackQuery):
    await callback.answer('Вы выбрали категорию')
    await callback.message.answer('Выберите нужную тему', reply_markup=inline.tasks)   
    
@router.callback_query(F.data == 'solution')
async def solution(callback: CallbackQuery):
    await callback.answer('Вы выбрали категорию')
    await callback.message.answer('Выберите нужную тему', reply_markup=inline.task_solution)
    
@router.callback_query(F.data == 'multimedia')
async def multimedia(callback: CallbackQuery):
    await callback.answer('Вы выбрали категорию')
    await callback.message.answer('Выберите интересующую тему', reply_markup=inline.multimedia)
    
@router.callback_query(F.data == 'history')
async def history(callback: CallbackQuery):
    await callback.answer('Вы выбрали категорию')
    await callback.message.answer('Выберите нужную категорию', reply_markup=inline.hist_information)
    
@router.callback_query(F.data == 'dictionary')
async def dictionary(callback: CallbackQuery):
    await callback.answer('Вы выбрали категорию')
    await callback.message.answer('Выберите нужные определение',reply_markup=inline.dictionary)