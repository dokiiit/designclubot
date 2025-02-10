
import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.client.default import DefaultBotProperties  # ✅ Важно для parse_mode!

# 🔹 Твой токен и ID
TOKEN = "7761909906:AAGMeo-NH4RCwoQe_ruY2kwuORVxgLLhIoo"  # Замени на свой токен
ADMIN_ID = 1402620870  # Замени на свой Telegram ID (без кавычек)

# Включаем логирование
logging.basicConfig(level=logging.INFO)

# Создаём бота и диспетчер
bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode="HTML"))  # ✅ Исправлено!
dp = Dispatcher()

# 🔹 Клавиатура (правильный формат)
keyboard = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text="📩 Оставить заявку")]],
    resize_keyboard=True
)

# 📌 Обработчик сообщений
@dp.message()
async def handle_message(message: types.Message):
    if message.text == "/start":
        await message.answer("Привет! Отправьте заявку, и я передам её администратору.", reply_markup=keyboard)
    elif message.text == "📩 Оставить заявку":
        await message.answer("✏️ Введите вашу заявку (опишите проблему или вопрос).")
    else:
        username = f"@{message.from_user.username}" if message.from_user.username else f"ID: {message.from_user.id}"
        text = f"📩 Новая заявка от {username}:\n\n{message.text}"

        # Отправляем админу
        await bot.send_message(ADMIN_ID, text)

        # Подтверждение пользователю
        await message.answer("✅ Ваша заявка отправлена! Мы скоро свяжемся с вами.")

# 🔹 Функция для запуска бота
async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

# Запуск бота
if __name__ == "__main__":
    asyncio.run(main())  # ✅ Исправлено!
