from aiogram import Router, types, F
# from services.chatgpt_api import chatgpt_answer

router = Router()


@router.message(F.text == "🤖 Chatgpt")
async def chatgpt_handler(message: types.Message):
    await message.answer("Xozircha ishlamaydi☺️")



# @router.message(F.text)
# async def get_gpt_text(message: types.Message):
#     user_text = message.text
#     try:
#         gpt = chatgpt_answer(user_text)
#         await message.answer(gpt)
#     except Exception as e:
#         await message.answer("Javobni yuborishda xatolik❗❌")
