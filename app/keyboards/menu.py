from aiogram import types
from aiogram.filters.callback_data import CallbackData


class MainDataMenu(CallbackData, prefix="main"):
    slug: str


def kb_main_menu(msg: types.Message):
    """Основное меню"""
    teamlead = types.InlineKeyboardButton(
        text="Я Media buyer/Team Lead и хочу к вам присоединиться",
        callback_data=MainDataMenu(slug="buyer-teamlead").pack(),
    )
    vacancy = types.InlineKeyboardButton(
        text="Посмотреть другие вакансии", callback_data=MainDataMenu(slug="other-vacanies").pack()
    )

    return types.InlineKeyboardMarkup(
        inline_keyboard=[[teamlead], [vacancy]],
    )
