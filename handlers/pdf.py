import os

from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext
from aiogram.types import FSInputFile

from states.pdf_state import PdfState
from services.pdf_builder import create_pdf


router = Router()

@router.message(F.text == "📁 PDF")
async def pdf_start(message: types.Message, state: FSMContext):
    await message.answer("📄 PDF nomini kiriting:")
    await state.set_state(PdfState.file_name)


@router.message(PdfState.file_name)
async def get_pdf_name(message: types.Message, state: FSMContext):
    await state.update_data(file_name=message.text)
    await message.answer("📝 PDF sarlavhasini kiriting:")
    await state.set_state(PdfState.title)


@router.message(PdfState.title)
async def get_title(message: types.Message, state: FSMContext):
    await state.update_data(title=message.text, contents=[])
    await message.answer(
        "✍️ Matn yoki 🖼 rasm yuboring.\n"
        "Tayyor bo'lsa 👉 <b>PDF tayyorla</b> deb yozing",
        parse_mode="HTML"
    )
    await state.set_state(PdfState.content)


@router.message(PdfState.content)
async def collect_content(message: types.Message, state: FSMContext):
    data = await state.get_data()
    contents = data["contents"]

    if message.text == "PDF tayyorla":
        pdf_path = create_pdf(
            file_name=data["file_name"],
            title=data["title"],
            contents=contents
        )

        # 📤 PDF yuboramiz
        await message.answer_document(
            FSInputFile(pdf_path),
            caption="✅ PDF tayyor bo'ldi"
        )

        # 🧹 RASMLARNI O'CHIRAMIZ
        for item_type, value in contents:
            if item_type == "image" and os.path.exists(value):
                os.remove(value)

        # 🧹 PDFNI O'CHIRAMIZ
        if os.path.exists(pdf_path):
            os.remove(pdf_path)

        await state.clear()
        return

    # ➕ TEXT
    if message.text:
        contents.append(("text", message.text))

    # ➕ IMAGE
    if message.photo:
        os.makedirs("temp", exist_ok=True)

        file = await message.bot.get_file(message.photo[-1].file_id)
        path = f"temp/{message.photo[-1].file_id}.jpg"

        await message.bot.download_file(file.file_path, path)
        contents.append(("image", path))

    await state.update_data(contents=contents)
    await message.answer("➕ Qo'shildi")


