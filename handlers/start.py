from aiogram import Router, F, types
from aiogram.filters import CommandStart

from database.crud import add_user, get_user
from keyboards.default import phone_number_btn, main_menu


router = Router()


@router.message(CommandStart())
async def start_hendler(message: types.Message):
    user_id = message.from_user.id
    user = get_user(user_id)

    if user:
        await message.answer("Menulardan birini tanlang👇", reply_markup=main_menu)
    else:
        full_name = message.from_user.full_name
        await message.answer(f"Assalomu alaykum hurmatli <b>{full_name}</b> Botimizga xush kelibsiz\nBotimizdan to'liq foydalanish uchun ro'yxatdan o'ting👇", reply_markup=phone_number_btn)



@router.message(F.contact)
async def get_user_contact(message: types.Message):
    user_id = message.from_user.id
    full_name = message.from_user.full_name
    username = message.from_user.username
    phone_number = message.contact.phone_number
    add_user(user_id, full_name, username, phone_number)
    await message.answer("Ro'yxatdan muaffaqqiyatli o'tildi\nBotdan bemalol foydalaning Menulardan birini tanlang👇", reply_markup=main_menu)