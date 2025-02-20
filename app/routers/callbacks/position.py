from app.core.logger import get_logger
from aiogram import Router, types, F
from app.keyboards.position import PositionMenu, Position

from app.keyboards.backbtn import btn_back_to_menu
from aiogram.fsm.context import FSMContext
from app.states.survey import SurveyData

router = Router(name=__name__)
logger = get_logger(__name__)


@router.callback_query(
    PositionMenu.filter(F.name.in_([Position.JUNIOR, Position.MIDDLE, Position.SENIOR, Position.LEAD]))
)
async def handle_jun_senior(callback_query: types.CallbackQuery, callback_data: PositionMenu, state: FSMContext):
    """
    Обработка диалога
    """
    await callback_query.answer()
    await state.update_data(position=callback_data.name)
    await state.set_state(SurveyData.name)
    await callback_query.message.answer(
        "Напиши свое имя:", reply_markup=types.InlineKeyboardMarkup(inline_keyboard=[[btn_back_to_menu()]])
    )
