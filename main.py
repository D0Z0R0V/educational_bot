import asyncio, os
from aiogram import Bot, Dispatcher

from dotenv import load_dotenv
from handlers import bot_message
from callback import (callback_class, 
                      callback_tasks, 
                      pagination,
                      callback_slovar)

load_dotenv()

async def main():
    bot = Bot(token=os.environ.get('BOT_TOKEN'), parse_mode="HTML")
    dp = Dispatcher()
    
    dp.include_routers(
        bot_message.router,
        callback_tasks.router,
        pagination.router,
        callback_class.router,
        callback_slovar.router
    )
    
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
    
if __name__ == "__main__":
    asyncio.run(main())