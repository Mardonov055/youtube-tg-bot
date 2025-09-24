from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import yt_dlp

BOT_TOKEN = "8339709824:AAEmSUjaFGAwC99nKbpEUTMr2iIlwO8t0C0"
ADMIN_USERNAME = "Mardonov055"  # Admin username

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer("👋 Salom! Menga YouTube link yuboring, men uni yuklab beraman 🎥")

@dp.message_handler()
async def download_video(message: types.Message):
    url = message.text.strip()
    try:
        ydl_opts = {
            'format': 'best',
            'outtmpl': 'video.mp4'
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        await message.answer("✅ Video yuklab olindi (lekin hozircha faqat serverga saqlanadi).")
    except Exception as e:
        # Xatolik bo‘lsa admin tugmasi chiqadi
        keyboard = InlineKeyboardMarkup().add(
            InlineKeyboardButton("✉️ Admin bilan bog‘lanish", url=f"https://t.me/{ADMIN_USERNAME}")
        )
        await message.answer(
            "❌ Xatolik yuz berdi. Quyidagi tugma orqali admin bilan bog‘lanishingiz mumkin:",
            reply_markup=keyboard
        )

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)