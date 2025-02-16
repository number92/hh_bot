from app.core.logger import get_logger
from aiogram import Router, types, F
from app.keyboards.menu import MainDataMenu
from app.keyboards.vacancies import VacancyData
from app.core.config import HH_EMPLOYER_ID
from app.keyboards.vacancies import kb_vacancies_upload_resume, kb_vacancies_view
from app.api_hh.hh_client import get_hh_client
from app.routers.messages import list_vacancies_view, make_message_vacancy

router = Router(name=__name__)
logger = get_logger(__name__)


@router.callback_query(MainDataMenu.filter(F.slug == "other-vacanies"))
async def handle_other_vacancies(callback_query: types.CallbackQuery, callback_data: MainDataMenu):
    """
    -- Посмотреть другие вакансии.
    """
    async with get_hh_client() as hh_api:
        response = await hh_api.get_vacancies_by_employer_id(HH_EMPLOYER_ID)

    return await callback_query.message.edit_text(
        text=list_vacancies_view(),
        reply_markup=kb_vacancies_view(response.items),
    )


@router.callback_query(VacancyData.filter(F.action == "view"))
async def handle_show_vacancy(callback_query: types.CallbackQuery, callback_data: VacancyData):
    async with get_hh_client() as hh_api:
        vacancy = await hh_api.get_vacancy(callback_data.id)
        print(vacancy.id)
    view = make_message_vacancy(vacancy)
    return await callback_query.message.answer(text=view, parse_mode="HTML")
