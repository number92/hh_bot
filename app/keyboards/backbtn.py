from aiogram import types


def btn_back_to_menu():
    return types.InlineKeyboardButton(text="Назад", callback_data="back-main")
