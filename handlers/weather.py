from aiogram import Router, F, types
from aiogram.types import FSInputFile
from aiogram.fsm.context import FSMContext


from services.weather_api import get_weather
from database.crud import update_city, get_user_city
from keyboards.default import city_keyboard
from states.weather import WeatherState

router = Router()


@router.message(F.text == "🌦 Ob-havo")
async def weather_handler(message: types.Message, state: FSMContext):
    last_city = get_user_city(message.from_user.id)

    await message.answer(
        "🏙 Qaysi shahar ob-havosini bilmoqchisiz?",
        reply_markup=city_keyboard(last_city)
    )
    await state.set_state(WeatherState.city_name)


@router.message(WeatherState.city_name, F.text)
async def get_city(message: types.Message, state: FSMContext):
    city = message.text.strip()

    data = await get_weather(city)
    if not data:
        await message.answer("❌ Shahar topilmadi, qayta urinib ko'ring")
        await state.clear()
        return

    # shaharni saqlab qo‘yamiz
    update_city(message.from_user.id, city)

    await message.answer_photo(
        photo=FSInputFile(data["image"]),
        caption=data["text"],
        parse_mode="HTML"
    )
    await state.clear()
