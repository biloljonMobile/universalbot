from aiogram.fsm.state import StatesGroup, State

class PdfState(StatesGroup):
    file_name = State()
    title = State()
    content = State()
