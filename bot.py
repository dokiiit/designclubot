import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Твой токен и ID
TOKEN = "7761909906:AAGMeo-NH4RCwoQe_ruY2kwuORVxgLLhIoo"  # Замени на свой токен
ADMIN_ID = 1402620870  # Замени на свой Telegram ID

# Включаем логирование
logging.basicConfig(level=logging.INFO)

# Создаём бота и диспетчер
bot = Bot(token=TOKEN, parse_mode="HTML")  # Используем правильный способ для parse_mode
dp = Dispatcher(bot)

# Клавиатура (правильный формат)
keyboard = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text="📩 Оставить заявку")]],
    resize_keyboard=True
)

# 📌 Обработчик команды /start
@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.answer("Привет! Отправьте заявку, и я передам её администратору.", reply_markup=keyboard)

# Обработчик для заявки
@dp.message_handler(lambda message: message.text == "📩 Оставить заявку")
async def request_application(message: types.Message):
    await message.answer("✏️ Введите вашу заявку (опишите проблему или вопрос).")

# Обработчик для получения заявки
@dp.message_handler()
async def receive_application(message: types.Message):
    username = f"@{message.from_user.username}" if message.from_user.username else f"ID: {message.from_user.id}"
    text = f"📩 Новая заявка от {username}:\n\n{message.text}"

    # Отправка заявки админу
    await bot.send_message(ADMIN_ID, text)

    # Подтверждение пользователю
    await message.answer("✅ Ваша заявка отправлена! Мы скоро свяжемся с вами.")

# Функция для запуска бота
async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling()  # Правильный способ для старта polling

# Запуск бота
if __name__ == "__main__":
    asyncio.run(main())  # Запуск асинхронного main
