from aiogram import Bot, Dispatcher, types
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder
import asyncio

# ================= НАСТРОЙКИ =================
BOT_TOKEN = "8875018275:AAGRimeltrRLKe0ClKkOhP7YnsNN554RCnI"

# Ссылки
CHANNEL_LINK = "https://t.me/tghublive"     # ← Замени
CHAT_LINK = "https://t.me/+9rx6Z1yOiFU1ZWUy"         # ← Замени если есть

WELCOME_TEXT = """
👋 Привет! Рад тебя видеть!

Ты пришёл из TikTok? 🔥

Теперь ты в нашем Telegram пространстве.

Здесь будет всё самое интересное:
• Новые видео и контент
• Общение
• Полезные материалы

Нажимай на кнопки ниже 👇
"""

# ============================================

bot = Bot(
    token=BOT_TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)

dp = Dispatcher()

def get_main_keyboard():
    builder = InlineKeyboardBuilder()
    builder.button(text="📢 Перейти в Канал", url=CHANNEL_LINK)
    if CHAT_LINK:
        builder.button(text="💬 Перейти в Чат", url=CHAT_LINK)
    builder.button(text="🔄 Обновить меню", callback_data="refresh")
    builder.adjust(1)
    return builder.as_markup()

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer(WELCOME_TEXT, reply_markup=get_main_keyboard())

@dp.callback_query(lambda c: c.data == "refresh")
async def refresh_menu(callback: types.CallbackQuery):
    await callback.message.edit_text(WELCOME_TEXT, reply_markup=get_main_keyboard())
    await callback.answer()

@dp.message()
async def all_messages(message: types.Message):
    if "tiktok" in message.text.lower() or "тикток" in message.text.lower():
        await message.answer("✅ Круто, что ты из TikTok! Добро пожаловать ❤️\n\n" + WELCOME_TEXT, 
                           reply_markup=get_main_keyboard())
    else:
        await message.answer("👋 Используй команду /start", reply_markup=get_main_keyboard())

async def main():
    print("✅ Бот успешно запущен и готов принимать людей с TikTok!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())