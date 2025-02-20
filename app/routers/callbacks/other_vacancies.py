from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext

from app.core.logger import get_logger
from app.keyboards.backbtn import btn_back_to_menu
from app.keyboards.menu import MainDataMenu
from app.keyboards.vacancies import (
    VacancyData,
    UploadResumeData,
    kb_upload_resume_and_back,
    kb_vacancies_upload_resume,
    kb_vacancies_view,
)
from app.core.config import HH_EMPLOYER_ID
from app.api_hh.hh_client import get_hh_client
from app.routers.messages import choose_position_message, list_vacancies_view, make_message_vacancy
from app.states.upload_resume import UploadResume

router = Router(name=__name__)
logger = get_logger(__name__)


@router.callback_query(MainDataMenu.filter(F.slug == "other-vacanies"))
async def handle_other_vacancies(callback_query: types.CallbackQuery, callback_data: MainDataMenu):
    """
    -- Посмотреть другие вакансии.
    """
    await callback_query.answer()
    async with get_hh_client() as hh_api:
        response = await hh_api.get_vacancies_by_employer_id(HH_EMPLOYER_ID)
    response.modify_vacancy_unique_names()
    return await callback_query.message.edit_text(
        text=list_vacancies_view(),
        reply_markup=kb_vacancies_view(response.items),
    )


@router.callback_query(UploadResumeData.filter(~F.id))
async def handle_upload_resume(callback_query: types.CallbackQuery):
    """(Нажал кнопку загрузить резюме из общего меню)"""
    await callback_query.answer()
    async with get_hh_client() as hh_api:
        response = await hh_api.get_vacancies_by_employer_id(HH_EMPLOYER_ID)
    response.modify_vacancy_unique_names()
    return await callback_query.message.edit_text(
        text=choose_position_message(),
        reply_markup=kb_vacancies_upload_resume(response.items),
    )


@router.callback_query(UploadResumeData.filter(F.id))
async def handle_upload_resume_with_known_position(
    callback_query: types.CallbackQuery, callback_data: UploadResumeData, state: FSMContext
):
    """(Нажал кнопку загрузить резюме после конкретной вакансии)"""
    await callback_query.answer()
    await state.update_data(for_vacancy=callback_data.id)
    await state.set_state(UploadResume.waiting_for_resume)
    return await callback_query.message.answer(
        text="Пожалуйста, отправь свое резюме в формате документа.",
        reply_markup=types.InlineKeyboardMarkup(inline_keyboard=[[btn_back_to_menu()]]),
    )


@router.callback_query(VacancyData.filter(F.action == "view"))
async def handle_show_vacancy(callback_query: types.CallbackQuery, callback_data: VacancyData):
    """(Нажал кнопку конкретной вакансии)"""
    await callback_query.answer()
    async with get_hh_client() as hh_api:
        vacancy = await hh_api.get_vacancy(callback_data.id)

    view = make_message_vacancy(vacancy)
    return await callback_query.message.answer(text=view, reply_markup=kb_upload_resume_and_back(id=vacancy.id))


@router.callback_query(VacancyData.filter(F.action == "upload"))
async def handle_show_vacancy_for_upload(
    callback_query: types.CallbackQuery, callback_data: VacancyData, state: FSMContext
):
    """(Нажал кнопку конкретной вакансии для загрузки резюме)"""
    await callback_query.answer()

    await state.update_data(for_vacancy=callback_data.id)
    await state.set_state(UploadResume.waiting_for_resume)
    return await callback_query.message.answer(
        text="Пожалуйста, отправь свое резюме в формате документа.",
        reply_markup=types.InlineKeyboardMarkup(inline_keyboard=[[btn_back_to_menu()]]),
    )
