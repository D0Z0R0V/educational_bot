from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

import app.keyboard as kb

router = Router()


class Register(StatesGroup):
    name = State()
    age = State()
    number = State()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer_sticker(sticker='CAACAgIAAxkBAAEL_bFmK1wHzF7Lm-Kg415zk-5St4Tn-AACYw4AAgtaoEg7Cb-9icYZzTQE')
    await message.answer('Привет!\n Я твой помощник в мире физике, пожалуйста выбери\
        интересующую тебя тему', reply_markup=kb.main)


@router.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer('Вы воспользовались кнопкой помощи')


@router.message(F.text == '7 класс')
async def button_7_class(message: Message):
    await message.answer('Выберите нужную тему', reply_markup=kb.class_7)
    
@router.message(F.text == '9 класс')
async def button_9_class(message: Message):
    await message.answer('Выберите нужную тему', reply_markup=kb.class_9)
    
@router.message(F.text == '10 класс')
async def button_10_class(message: Message):
    await message.answer('Выберите нужную тему', reply_markup=kb.class_10)
    
@router.message(F.text == 'Приложения')
async def apps(message: Message):
    await message.answer('Выберите нужную тему', reply_markup=kb.apps)
    
@router.callback_query(F.data == 'test_tasks')
async def query_7_class(callback: CallbackQuery):
    await callback.answer('Вы выбрали категорию')
    await callback.message.answer('Выберите нужную тему', reply_markup=kb.test_class)
    
@router.callback_query(F.data == 'tasks')
async def task(callback: CallbackQuery):
    await callback.answer('Вы выбрали категорию')
    await callback.message.answer('Выберите нужную тему', reply_markup=kb.tasks)   
    
@router.callback_query(F.data == 'solution')
async def solution(callback: CallbackQuery):
    await callback.answer('Вы выбрали категорию')
    await callback.message.answer('Выберите нужную тему', reply_markup=kb.task_solution)
    
@router.callback_query(F.data == 'multimedia')
async def multimedia(callback: CallbackQuery):
    await callback.answer('Вы выбрали категорию')
    await callback.message.answer('Выберите интересующую тему', reply_markup=kb.multimedia)
    
@router.callback_query(F.data == 'history')
async def history(callback: CallbackQuery):
    await callback.answer('Вы выбрали категорию')
    await callback.message.answer('Выберите нужную категорию', reply_markup=kb.hist_information)
    
@router.callback_query(F.data == 'dictionary')
async def dictionary(callback: CallbackQuery):
    await callback.answer('Вы выбрали категорию')
    await callback.message.answer('Выберите нужные определение',reply_markup=kb.dictionary)

    

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


@router.message(Command('register'))
async def register(message: Message, state: FSMContext):
    await state.set_state(Register.name)
    await message.answer('Введите ваше имя')


@router.message(Register.name)
async def register_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Register.age)
    await message.answer('Введите ваш возраст')


@router.message(Register.age)
async def register_age(message: Message, state: FSMContext):
    await state.update_data(age=message.text)
    await state.set_state(Register.number)
    await message.answer('Отправьте ваш номер телефона', reply_markup=kb.get_number)


@router.message(Register.number, F.contact)
async def register_number(message: Message, state: FSMContext):
    await state.update_data(number=message.contact.phone_number)
    data = await state.get_data()
    await message.answer(f'Ваше имя: {data["name"]}\nВаш возраст: {data["age"]}\nНомер: {data["number"]}')
    await state.clear()