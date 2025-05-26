from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InputFile
import logging
import os

API_TOKEN = os.getenv("BOT_TOKEN")

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    arg = message.get_args()
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

    file_name = f"МАЙнинг_{level_titles.get(arg, '')}.pdf" if arg in level_titles else None
    if file_name and os.path.exists(f"pdf/{file_name}"):
        await message.answer(f"👋 Привет! Твой уровень — {level_titles[arg]}.")
        await message.answer("📄 Вот твоя PDF-инструкция:")
        await message.answer_document(InputFile(f"pdf/{file_name}"))
    else:
        await message.answer("👋 Привет! Добро пожаловать в МАЙнинг. Начни с прохождения анкеты: https://yasleep.ru/mining")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
