from googletrans import Translator
from gtts import gTTS
import os
import uuid

translator = Translator()

AUDIO_DIR = "voices"
os.makedirs(AUDIO_DIR, exist_ok=True)


async def translate_text(text: str, dest_lang: str = "en") -> str:
    result = await translator.translate(text, dest=dest_lang)
    return result.text


def text_to_speech(text: str, lang: str = "en") -> str:
    """
    Matndan audio yaratadi va fayl path qaytaradi
    """
    filename = f"{uuid.uuid4()}.mp3"
    file_path = os.path.join(AUDIO_DIR, filename)

    tts = gTTS(text=text, lang=lang)
    tts.save(file_path)

    return file_path
