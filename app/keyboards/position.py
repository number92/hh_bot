from aiogram import types
from app.keyboards.backbtn import btn_back_to_menu
from aiogram.filters.callback_data import CallbackData


class Position:
    JUNIOR = "Junior"
    MIDDLE = "Middle"
    SENIOR = "Senior"


class PosititonMenu(CallbackData, prefix="position"):
    name: str


def kb_choose_position():

    jun = types.InlineKeyboardButton(text=Position.JUNIOR, callback_data=PosititonMenu(name=Position.JUNIOR).pack())
    mid = types.InlineKeyboardButton(text=Position.MIDDLE, callback_data=PosititonMenu(name=Position.MIDDLE).pack())
    sen = types.InlineKeyboardButton(text=Position.SENIOR, callback_data=PosititonMenu(name=Position.SENIOR).pack())
    lead = types.InlineKeyboardButton(text="Team Lead", callback_data="lead")
    back = btn_back_to_menu()
    return types.InlineKeyboardMarkup(
        inline_keyboard=[[jun], [mid], [sen], [lead], [back]],
    )
