import asyncio
import logging

from aiogram import Bot, Dispatcher
from config import TOKEN
from aiogram.client.default import DefaultBotProperties

from database.crud import init_db
from handlers import start, instagram, translate, weather, prayer, chatgpt, pdf, admin


logging.basicConfig(level=logging.INFO)


async def main():
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode="HTML"))
    dp = Dispatcher()

    init_db()

    dp.include_router(start.router)
    dp.include_router(instagram.router)
    dp.include_router(translate.router)
    dp.include_router(weather.router)
    dp.include_router(prayer.router)
    dp.include_router(chatgpt.router)
    dp.include_router(pdf.router)
    dp.include_router(admin.router)

    await dp.start_polling(bot)



if __name__ == "__main__":
    asyncio.run(main())