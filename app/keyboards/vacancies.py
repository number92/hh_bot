from aiogram import types
from app.keyboards.backbtn import btn_back_to_menu
from aiogram.filters.callback_data import CallbackData
from aiogram.utils.keyboard import InlineKeyboardBuilder


class Position:
    JUNIOR = "Junior"
    MIDDLE = "Middle"
    SENIOR = "Senior"
    LEAD = "Team Lead"


class PositionMenu(CallbackData, prefix="position"):
    name: str


def kb_other_vacancies():
    builder = InlineKeyboardBuilder()


# TODO: клавиатура
