from app.core.logger import get_logger
from aiogram import Router, types, F
from app.keyboards.menu import MainDataMenu
from app.core.config import HH_EMPLOYER_ID
from app.keyboards.vacancies import kb_vacancies_upload_resume, kb_vacancies_view
from app.api_hh.hh_client import get_hh_client

router = Router(name=__name__)
logger = get_logger(__name__)


@router.callback_query(MainDataMenu.filter(F.slug == "other-vacanies"))
async def handle_other_vacancies(callback_query: types.CallbackQuery, callback_data: MainDataMenu):
    """
    -- Посмотреть другие вакансии.
    """
    msg = """
           Ниже можно ознакомиться с открытыми вакансиями.
            Если вдруг не нашел подходящей позиции, загрузи свое резюме, и мы обязательно его рассмотрим!
           """
    async with get_hh_client() as hh_api:
        response = await hh_api.get_vacancies_by_employer_id(HH_EMPLOYER_ID)

    return await callback_query.message.edit_text(
        text=msg,
        reply_markup=kb_vacancies_view(response.items),
    )
