from app.core.logger import get_logger
from aiogram import Router, types, F
from app.keyboards.source_work import SourceData, SourceWork
from app.keyboards.backbtn import btn_back_to_menu
from aiogram.fsm.context import FSMContext
from app.states.survey import SurveyData


router = Router(name=__name__)
logger = get_logger(__name__)


@router.callback_query(SourceData.filter(F.name))
async def handle_source_work(callback_query: types.CallbackQuery, callback_data: SourceData, state: FSMContext):
    """
    -- Выбери свой источник
    """
    await callback_query.answer()
    await state.update_data(source=callback_data.name)
    if callback_data.name == SourceWork.FB:
        await state.set_state(state=SurveyData.geo)
        return await callback_query.message.answer(
            "С Каким ГЕО вы работаете?", reply_markup=types.InlineKeyboardMarkup(inline_keyboard=[[btn_back_to_menu()]])
        )
    await state.set_state(state=SurveyData.other_source)
    return await callback_query.message.answer(
        "Пожалуйста, напиши свой источник",
        reply_markup=types.InlineKeyboardMarkup(inline_keyboard=[[btn_back_to_menu()]]),
    )
