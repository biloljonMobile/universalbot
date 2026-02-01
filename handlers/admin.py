from math import ceil

from aiogram import Router, types, F
from aiogram.filters import Command

from datetime import datetime

from config import ADMIN_ID
from database.crud import get_users, users_count
from keyboards.inline import admin_pagination


router = Router()

USERS_PER_PAGE = 5


@router.message(Command("admin"))
async def admin_panel(message: types.Message):
    if message.from_user.id != ADMIN_ID:
        pass

    await send_users(message, page=1)



@router.callback_query(F.data.startswith("admin:"))
async def admin_pages(call: types.CallbackQuery):
    page = int(call.data.split(":")[1])
    await send_users(call, page)
    await call.answer()



async def send_users(message_or_call, page: int):
    total = users_count()
    total_pages = max(1, ceil(total / USERS_PER_PAGE))
    offset = (page - 1) * USERS_PER_PAGE

    users = get_users(offset=offset, limit=USERS_PER_PAGE)

    text = "👥 <b>Bot foydalanuvchilari:</b>\n\n"

    if not users:
        text += "Hozircha foydalanuvchilar yo'q 🤷‍♂️"
    else:
        for u in users:
            # Vaqtni chiroyli formatga o'tkazamiz
            raw_time = u[4]
            if raw_time:
                try:
                    dt = datetime.fromisoformat(raw_time)
                    nice_time = dt.strftime("%d.%m.%Y %H:%M")
                except Exception:
                    nice_time = "yo'q"
            else:
                nice_time = "yo'q"

            text += (
                f"🆔 <b>ID:</b> {u[0]}\n"
                f"👤 <b>Ism:</b> {u[1]}\n"
                f"🔗 <b>Username:</b> @{u[2] if u[2] else "yo'q"}\n"
                f"📞 <b>Telefon:</b> +{u[3] if u[3] else "yo'q"}\n"
                f"🕔 <b>Vaqti:</b> {nice_time}\n"
                f"———————————\n"
            )

    keyboard = admin_pagination(page, total_pages)

    if isinstance(message_or_call, types.Message):
        await message_or_call.answer(text, reply_markup=keyboard)
    else:
        await message_or_call.message.edit_text(text, reply_markup=keyboard)

