import aiohttp
from config import WEATHER_API


TRANSLATIONS = {
    "clear sky": "Ochiq osmon",
    "few clouds": "Yengil bulutli",
    "scattered clouds": "Tarqoq bulutlar",
    "broken clouds": "Qisman bulutli",
    "overcast clouds": "Bulutli",
    "light rain": "Yengil yomg'ir",
    "moderate rain": "O'rtacha yomg'ir",
    "heavy rain": "Kuchli yomg'ir",
    "shower rain": "Yomg'ir",
    "thunderstorm": "Momaqaldiroq",
    "snow": "Qor",
    "mist": "Tuman",
}

WEATHER_IMAGES = {
    "clear": "weather_img/sunny.png",
    "clouds": "weather_img/cloudy.png",
    "rain": "weather_img/rainy.png",
    "snow": "weather_img/snow.png",
    "thunderstorm": "weather_img/storm.png",
    "mist": "weather_img/fog.png",
}


async def get_weather(city: str):
    url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?q={city}&appid={WEATHER_API}&units=metric"
    )

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.json()

            if data.get("cod") != 200:
                return None

            weather_main = data["weather"][0]["main"].lower()
            desc_en = data["weather"][0]["description"].lower()
            desc = TRANSLATIONS.get(desc_en, desc_en.capitalize())

            image = WEATHER_IMAGES.get(weather_main, "weather_img/default.jpg")

            text = (
                f"🏙 <b>Shahar:</b> {data['name']}\n"
                f"🌤 <b>Holat:</b> {desc}\n"
                f"🌡 <b>Harorat:</b> {data['main']['temp']}°C\n"
                f"🤔 <b>Sezilishi:</b> {data['main']['feels_like']}°C\n"
                f"💧 <b>Namlik:</b> {data['main']['humidity']}%"
            )

            return {
                "text": text,
                "image": image
            }
