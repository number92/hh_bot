from aiogram import types
from app.keyboards.backbtn import btn_back_to_menu
from aiogram.filters.callback_data import CallbackData


class SourceWork:
    FB = "Facebook"
    OTHER = "Другой"


class SourceData(CallbackData, prefix="source"):
    name: str


def kb_choose_your_source():
    fb = types.InlineKeyboardButton(text=SourceWork.FB, callback_data=SourceData(name=SourceWork.FB).pack())
    other = types.InlineKeyboardButton(text=SourceWork.OTHER, callback_data=SourceData(name=SourceWork.OTHER).pack())
    back = btn_back_to_menu()
    return types.InlineKeyboardMarkup(
        inline_keyboard=[[fb, other], [back]],
    )
