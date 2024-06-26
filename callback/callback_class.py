from aiogram import Router, F, types
from aiogram.types import CallbackQuery
from aiogram.enums import ChatAction

from data.subloader import get_json_data
from keyboards import fabrics

router = Router()

@router.callback_query(F.data == "Gravity")
async def get_7_class(callback: CallbackQuery):
    smiles = await get_json_data("class7.json") 
    await callback.message.bot.send_chat_action(
        chat_id=callback.message.chat.id,
        action=ChatAction.UPLOAD_PHOTO
    )
     
    await callback.answer('Вы выбрали категорию')
    photo_path = smiles[0][0]
    caption = smiles[0][1]
    if photo_path:
        photo = types.FSInputFile(photo_path)
        await callback.message.answer_photo(
            photo=photo,
            caption=caption,
            reply_markup=fabrics.paginator(file_name="class7.json")
        )
    else:
        await callback.message.answer(
            text=caption,
            reply_markup=fabrics.paginator(file_name="class7.json")
        )

    
@router.callback_query(F.data == "Planets")
async def get_72_class(callback: CallbackQuery):
    smiles = await get_json_data("class72.json")
    await callback.message.bot.send_chat_action(
        chat_id=callback.message.chat.id,
        action=ChatAction.UPLOAD_PHOTO
    )
    
    await callback.answer('Вы выбрали категорию')
    photo_path = smiles[0][0]
    caption = smiles[0][1]
    if photo_path:
        photo = types.FSInputFile(photo_path)
        await callback.message.answer_photo(
            photo=photo,
            caption=caption,
            reply_markup=fabrics.paginator(file_name="class72.json")
        )
    else:
        await callback.message.answer(
            text=caption,
            reply_markup=fabrics.paginator(file_name="class72.json")
        )
   
@router.callback_query(F.data == "law")
async def get_9_class(callback: CallbackQuery):
    smiles = await get_json_data("class9.json")
    await callback.message.bot.send_chat_action(
        chat_id=callback.message.chat.id,
        action=ChatAction.UPLOAD_PHOTO
    )
    
    await callback.answer('Вы выбрали категорию')
    photo_path = smiles[0][0]
    caption = smiles[0][1]
    if photo_path:
        photo = types.FSInputFile(photo_path)
        await callback.message.answer_photo(
            photo=photo,
            caption=caption,
            reply_markup=fabrics.paginator(file_name="class9.json")
        )
    else:
        await callback.message.answer(
            text=caption,
            reply_markup=fabrics.paginator(file_name="class9.json")
        )
   
@router.callback_query(F.data == "boost")
async def get_92_class(callback: CallbackQuery):
    smiles = await get_json_data("class92.json")
    await callback.message.bot.send_chat_action(
        chat_id=callback.message.chat.id,
        action=ChatAction.UPLOAD_PHOTO
    )
    
    await callback.answer('Вы выбрали категорию')
    photo_path = smiles[0][0]
    caption = smiles[0][1]
    if photo_path:
        photo = types.FSInputFile(photo_path)
        await callback.message.answer_photo(
            photo=photo,
            caption=caption,
            reply_markup=fabrics.paginator(file_name="class92.json")
        )
    else:
        await callback.message.answer(
            text=caption,
            reply_markup=fabrics.paginator(file_name="class92.json")
        )
   
@router.callback_query(F.data == "artificial_satellites")
async def get_93_class(callback: CallbackQuery):
    smiles = await get_json_data("class93.json")
    await callback.message.bot.send_chat_action(
        chat_id=callback.message.chat.id,
        action=ChatAction.UPLOAD_PHOTO
    )
    
    await callback.answer('Вы выбрали категорию')
    photo_path = smiles[0][0]
    caption = smiles[0][1]
    if photo_path:
        photo = types.FSInputFile(photo_path)
        await callback.message.answer_photo(
            photo=photo,
            caption=caption,
            reply_markup=fabrics.paginator(file_name="class93.json")
        )
    else:
        await callback.message.answer(
            text=caption,
            reply_markup=fabrics.paginator(file_name="class93.json")
        )
   
@router.callback_query(F.data == '_universal_gravity')
async def get_10_class(callback: CallbackQuery):
    smiles = await get_json_data("class10.json")
    await callback.message.bot.send_chat_action(
        chat_id=callback.message.chat.id,
        action=ChatAction.UPLOAD_PHOTO
    )
    
    await callback.answer('Вы выбрали категорию')
    photo_path = smiles[0][0]
    caption = smiles[0][1]
    if photo_path:
        photo = types.FSInputFile(photo_path)
        await callback.message.answer_photo(
            photo=photo,
            caption=caption,
            reply_markup=fabrics.paginator(file_name="class10.json")
        )
    else:
        await callback.message.answer(
            text=caption,
            reply_markup=fabrics.paginator(file_name="class10.json")
        )
   
@router.callback_query(F.data == 'other_planets')
async def get_102_class(callback: CallbackQuery):
    smiles = await get_json_data("class102.json")
    await callback.message.bot.send_chat_action(
        chat_id=callback.message.chat.id,
        action=ChatAction.UPLOAD_PHOTO
    )
    
    await callback.answer('Вы выбрали категорию')
    photo_path = smiles[0][0]
    caption = smiles[0][1]
    if photo_path:
        photo = types.FSInputFile(photo_path)
        await callback.message.answer_photo(
            photo=photo,
            caption=caption,
            reply_markup=fabrics.paginator(file_name="class102.json")
        )
    else:
        await callback.message.answer(
            text=caption,
            reply_markup=fabrics.paginator(file_name="class102.json")
        )
    
@router.callback_query(F.data == 'first_speed')
async def get_103_class(callback: CallbackQuery):
    smiles = await get_json_data("class103.json")
    await callback.message.bot.send_chat_action(
        chat_id=callback.message.chat.id,
        action=ChatAction.UPLOAD_PHOTO
    )
    
    await callback.answer('Вы выбрали категорию')
    photo_path = smiles[0][0]
    caption = smiles[0][1]
    if photo_path:
        photo = types.FSInputFile(photo_path)
        await callback.message.answer_photo(
            photo=photo,
            caption=caption,
            reply_markup=fabrics.paginator(file_name="class103.json")
        )
    else:
        await callback.message.answer(
            text=caption,
            reply_markup=fabrics.paginator(file_name="class103.json")
        )
   
    
@router.callback_query(F.data == 'abstract')
async def get_consp_class(callback: CallbackQuery):
    smiles = await get_json_data("consp.json")
    await callback.message.bot.send_chat_action(
        chat_id=callback.message.chat.id,
        action=ChatAction.UPLOAD_PHOTO
    )
    
    await callback.answer('Вы выбрали категорию')
    photo_path = smiles[0][0]
    caption = smiles[0][1]
    if photo_path:
        photo = types.FSInputFile(photo_path)
        await callback.message.answer_photo(
            photo=photo,
            caption=caption,
            reply_markup=fabrics.paginator(file_name="consp.json")
        )
    else:
        await callback.message.answer(
            text=caption,
            reply_markup=fabrics.paginator(file_name="consp.json")
        )

@router.callback_query(F.data == 'task_OGE')
async def get_task_OGE(callback: CallbackQuery):
    smiles = await get_json_data('OGE.json')
    await callback.answer('Вы выбрали категорию')
    photo_path = smiles[0][0]
    caption = smiles[0][1]
    if photo_path:
        photo = types.FSInputFile(photo_path)
        await callback.message.answer_photo(
            photo=photo,
            caption=caption,
            reply_markup=fabrics.paginator(file_name="OGE.json")
        )
    else:
        await callback.message.answer(
            text=caption,
            reply_markup=fabrics.paginator(file_name="OGE.json")
        )
   
@router.callback_query(F.data == 'task_EGE')
async def get_task_EGE(callback: CallbackQuery):
    smiles = await get_json_data('EGE.json')
    await callback.answer('Вы выбрали категорию')
    photo_path = smiles[0][0]
    caption = smiles[0][1]
    if photo_path:
        photo = types.FSInputFile(photo_path)
        await callback.message.answer_photo(
            photo=photo,
            caption=caption,
            reply_markup=fabrics.paginator(file_name="EGE.json")
        )
    else:
        await callback.message.answer(
            text=caption,
            reply_markup=fabrics.paginator(file_name="EGE.json")
        )
   
@router.callback_query(F.data == 'level_A')
async def get_level_A(callback: CallbackQuery):
    smiles = await get_json_data('level_A.json')
    await callback.answer('Вы выбрали категорию')
    photo_path = smiles[0][0]
    caption = smiles[0][1]
    if photo_path:
        photo = types.FSInputFile(photo_path)
        await callback.message.answer_photo(
            photo=photo,
            caption=caption,
            reply_markup=fabrics.paginator(file_name="level_A.json")
        )
    else:
        await callback.message.answer(
            text=caption,
            reply_markup=fabrics.paginator(file_name="level_A.json")
        )
   
@router.callback_query(F.data == 'level_B')
async def get_level_B(callback: CallbackQuery):
    smiles = await get_json_data('level_B.json')
    await callback.answer('Вы выбрали категорию')
    photo_path = smiles[0][0]
    caption = smiles[0][1]
    if photo_path:
        photo = types.FSInputFile(photo_path)
        await callback.message.answer_photo(
            photo=photo,
            caption=caption,
            reply_markup=fabrics.paginator(file_name="level_B.json")
        )
    else:
        await callback.message.answer(
            text=caption,
            reply_markup=fabrics.paginator(file_name="level_B.json")
        )
   
@router.callback_query(F.data == 'level_C')
async def get_level_C(callback: CallbackQuery):
    smiles = await get_json_data('level_C.json')
    await callback.answer('Вы выбрали категорию')
    photo_path = smiles[0][0]
    caption = smiles[0][1]
    if photo_path:
        photo = types.FSInputFile(photo_path)
        await callback.message.answer_photo(
            photo=photo,
            caption=caption,
            reply_markup=fabrics.paginator(file_name="level_C.json")
        )
    else:
        await callback.message.answer(
            text=caption,
            reply_markup=fabrics.paginator(file_name="level_C.json")
        )
        
@router.callback_query(F.data == 'gif')
async def get_gif(callback: CallbackQuery):
    await callback.answer('Вы выбрали категорию')
    await callback.message.bot.send_chat_action(
        chat_id=callback.message.chat.id,
        action=ChatAction.UPLOAD_VIDEO
    )
          
    await callback.message.answer_document(document=types.FSInputFile(
        path='data/application/gif_2.gif'
    ))
