from aiogram.fsm.state import StatesGroup, State

class TranslateState(StatesGroup):
    text = State()
    language = State()
