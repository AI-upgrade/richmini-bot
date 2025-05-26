import os
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.types import InputFile
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.client.default import DefaultBotProperties
from aiogram import F

from aiogram import Router
from aiogram.types import Message
from aiogram.utils.markdown import hbold
import asyncio

BOT_TOKEN = os.getenv("BOT_TOKEN")

logging.basicConfig(level=logging.INFO)

dp = Dispatcher(storage=MemoryStorage())
bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

@dp.message(F.text.startswith("/start"))
async def send_welcome(message: types.Message):
    arg = message.text.split(maxsplit=1)[-1] if len(message.text.split()) > 1 else ""
    level_titles = {
        "color_beige": "Бежевый",
        "color_purple": "Фиолетовый",
        "color_red": "Красный",
        "color_blue": "Синий",
        "color_orange": "Оранжевый",
        "color_green": "Зелёный",
        "color_yellow": "Жёлтый",
        "color_turquoise": "Бирюзовый"
    }

    title = level_titles.get(arg)
    if title:
        file_path = f"pdf/МАЙнинг_{title}.pdf"
        if os.path.exists(file_path):
            await message.answer(f"👋 Привет! Твой уровень — <b>{title}</b>.\n📄 Вот твоя PDF-инструкция:")
            await message.answer_document(InputFile(file_path))
            return

    await message.answer("👋 Добро пожаловать в МАЙнинг.\nПройди анкету: https://yasleep.ru/mining")

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
