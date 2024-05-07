import asyncio, os
from aiogram import Bot, Dispatcher

from handlers import router
from dotenv import load_dotenv
from handlers import bot_message
from callback import callback_class, callback_tasks

load_dotenv()

async def main():
    bot = Bot(token=os.environ.get('BOT_TOKEN'))
    dp = Dispatcher()
    dp.include_router(
        bot_message.router,
        callback_tasks.router,
        callback_tasks.router
    )
    await dp.start_polling(bot)
    
if __name__ == "__main__":
    asyncio.run(main())