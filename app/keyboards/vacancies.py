from typing import List
from aiogram import types
from app.keyboards.backbtn import btn_back_to_menu
from aiogram.filters.callback_data import CallbackData
from aiogram.utils.keyboard import InlineKeyboardBuilder
from app.api_hh.entities import Vacancy


class VacancyData(CallbackData, prefix="vacancy"):
    id: str
    action: str


class UploadResume(CallbackData, prefix="resume"):
    name: str


def _builder_show_vacancies(data: List[Vacancy], action: str) -> InlineKeyboardBuilder:
    builder = InlineKeyboardBuilder()
    for vacancy in data:
        builder.add(
            types.InlineKeyboardButton(
                text=vacancy.name, callback_data=VacancyData(id=vacancy.id, action=action).pack()
            )
        )
    return builder


def kb_vacancies_view(data: List[Vacancy]):
    builder = _builder_show_vacancies(data, "view")
    builder.add(types.InlineKeyboardButton(text="Загрузить резюме", callback_data=UploadResume(name="upload").pack()))
    builder.add(btn_back_to_menu())
    builder.adjust(1)
    return builder.as_markup()


def kb_vacancies_upload_resume(data: List[Vacancy]):
    builder = _builder_show_vacancies(data, "upload")
    builder.add(btn_back_to_menu())
    builder.adjust(1)
    return builder.as_markup()
