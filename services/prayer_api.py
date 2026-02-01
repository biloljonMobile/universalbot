import aiohttp
from config import PRAYER_API


async def get_prayer_times():
    async with aiohttp.ClientSession() as session:
        async with session.get(PRAYER_API) as response:
            data = await response.json()

            timings = data["data"]["timings"]

            return {
                "Fajr": timings["Fajr"],
                "Sunrise": timings["Sunrise"],
                "Dhuhr": timings["Dhuhr"],
                "Asr": timings["Asr"],
                "Maghrib": timings["Maghrib"],
                "Isha": timings["Isha"],
            }
