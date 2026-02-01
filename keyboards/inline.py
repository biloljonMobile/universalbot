from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from keyboards.languages import LANGUAGES

PER_PAGE = 4


def language_pagination(page: int = 0):
    start = page * PER_PAGE
    end = start + PER_PAGE
    page_langs = LANGUAGES[start:end]

    buttons = [
        [InlineKeyboardButton(text=name, callback_data=f"lang:{code}")]
        for name, code in page_langs
    ]

    total_pages = (len(LANGUAGES) - 1) // PER_PAGE

    nav_buttons = []
    if page > 0:
        nav_buttons.append(
            InlineKeyboardButton(text="⬅️", callback_data=f"page:{page-1}")
        )

    nav_buttons.append(
        InlineKeyboardButton(
            text=f"{page+1}/{total_pages+1}",
            callback_data="ignore"
        )
    )

    if page < total_pages:
        nav_buttons.append(
            InlineKeyboardButton(text="➡️", callback_data=f"page:{page+1}")
        )

    buttons.append(nav_buttons)

    return InlineKeyboardMarkup(inline_keyboard=buttons)



def admin_pagination(page, total_pages):
    buttons = []

    if page > 1:
        buttons.append(
            InlineKeyboardButton(text="⬅️", callback_data=f"admin:{page-1}")
        )

    buttons.append(
        InlineKeyboardButton(text=f"{page}/{total_pages}", callback_data="noop")
    )

    if page < total_pages:
        buttons.append(
            InlineKeyboardButton(text="➡️", callback_data=f"admin:{page+1}")
        )

    return InlineKeyboardMarkup(inline_keyboard=[buttons])