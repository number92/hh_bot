from aiogram import types
from app.keyboards.backbtn import btn_back_to_menu
from aiogram.filters.callback_data import CallbackData


class Position:
    JUNIOR = "Junior"
    MIDDLE = "Middle"
    SENIOR = "Senior"
    LEAD = "Team Lead"


class PositionMenu(CallbackData, prefix="position"):
    name: str


def kb_choose_position():

    jun = types.InlineKeyboardButton(text=Position.JUNIOR, callback_data=PositionMenu(name=Position.JUNIOR).pack())
    mid = types.InlineKeyboardButton(text=Position.MIDDLE, callback_data=PositionMenu(name=Position.MIDDLE).pack())
    sen = types.InlineKeyboardButton(text=Position.SENIOR, callback_data=PositionMenu(name=Position.SENIOR).pack())
    lead = types.InlineKeyboardButton(text=Position.LEAD, callback_data=PositionMenu(name=Position.LEAD).pack())
    back = btn_back_to_menu()
    return types.InlineKeyboardMarkup(
        inline_keyboard=[[jun], [mid], [sen], [lead], [back]],
    )
