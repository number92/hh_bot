from aiogram import types
from aiogram.filters.callback_data import CallbackData


class MainDataMenu(CallbackData, prefix="main"):
    slug: str
    prev_mess: None | int


def kb_main_menu(msg: types.Message):
    """Основное меню"""
    teamlead = types.InlineKeyboardButton(
        text="Я Media buyer/Team Lead и хочу к вам присоединиться",
        callback_data=MainDataMenu(slug="buyer-teamlead", prev_mess=msg.message_id).pack(),
    )
    vacancy = types.InlineKeyboardButton(
        text="Посмотреть другие вакансии",
        callback_data=MainDataMenu(slug="other-vacanies", prev_mess=msg.message_id).pack(),
    )

    return types.InlineKeyboardMarkup(
        inline_keyboard=[[teamlead], [vacancy]],
    )
