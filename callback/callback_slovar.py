from aiogram import Router, F, types
from aiogram.types import CallbackQuery


router = Router()

@router.callback_query(F.data == 'power')
async def slovar1(callback: CallbackQuery):
    await callback.answer('Кнопка нажата')
    await callback.message.answer(text='Сила тяжести – сила, с которой\
        Земля притягивает к себе тело.')
    
@router.callback_query(F.data == 'universal_gravity')
async def slovar2(callback: CallbackQuery):
    await callback.answer('Кнопка нажата')
    await callback.message.answer(text='Всемирное тяготения – это притяжение всех тел Вселенной друг другу.')
    
@router.callback_query(F.data == 'gravitation')
async def slovar5(callback: CallbackQuery):
    await callback.answer('Кнопка нажата')
    await callback.message.answer(text='Гравитационные силы – это силы\
        взаимодействия между телами, которые зависят от их массы.')
    
@router.callback_query(F.data == 'satellites')
async def slovar6(callback: CallbackQuery):
    await callback.answer('Кнопка нажата')
    await callback.message.answer(text='Искусственный спутник Земли (ИСЗ) – тело,\
        движущееся по окружности вокруг Земли.')
    
@router.callback_query(F.data == 'law_gravity')
async def slovar3(callback: CallbackQuery):
    photo_path = 'data/photo_slovar/image.png'
    await callback.answer('Кнопка нажата')
    await callback.message.answer_photo(
        photo=types.FSInputFile(
            path=photo_path
        )
    )
    
@router.callback_query(F.data == 'cosmic_velocity')
async def slovar4(callback: CallbackQuery):
    photo_path = 'data/photo_slovar/photo.jpg'
    await callback.answer('Кнопка нажата')
    await callback.message.answer_photo(
        photo=types.FSInputFile(
            path=photo_path
        )
    )

@router.callback_query(F.data == 'constant_gr')
async def slovar6(callback: CallbackQuery):
    photo_path = 'data/photo_slovar/photo_2.jpg'
    await callback.answer('Кнопка нажата')
    await callback.message.answer_photo(
        photo=types.FSInputFile(
            path=photo_path
        )
    )
    
@router.callback_query(F.data == 'weight')
async def slovar7(callback: CallbackQuery):
    photo_list = ['data/photo_slovar/photo_31.jpg','data/photo_slovar/photo_32.jpg']
    await callback.answer('Кнопка нажата')
    for index in photo_list:
        await callback.message.answer_photo(
            photo=types.FSInputFile(
                path=index
            )
        )