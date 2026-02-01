import os

from aiogram import Router, F, types
from aiogram.types import FSInputFile
from services.instagram_loader import download_instagram_video

router = Router()


@router.message(F.text == "📥 Instagram")
async def instagram_hendler(message: types.Message):
    await message.answer("Instagram havolasini yuboring")




@router.message(F.text.startswith("http"))
async def get_instagram_url(message: types.Message):
    url = message.text

    if "instagram.com" not in url:
        await message.answer("❌ Bu Instagram havola emas")
        return

    msg = await message.answer("⏳ Video yuklanmoqda, kuting...")

    try:
        video_path = download_instagram_video(url)

        video = FSInputFile(video_path)
        await message.answer_video(video)

        # Faylni o‘chirish (ixtiyoriy, tavsiya qilaman)
        os.remove(video_path)

    except Exception as e:
        await message.answer("❌ Video yuklab bo'lmadi")
        print(e)

    await msg.delete()