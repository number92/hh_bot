from aiogram import F, Router, types
from aiogram.fsm.context import FSMContext
from app.states.survey import SurveyData

router = Router(name=__name__)


@router.message(SurveyData.count_workers, F.text)
async def handle_count_workers(message: types.Message, state: FSMContext):
    """-- Количество человек в команде"""
    await state.update_data(count_workers=message.text)
    await state.set_state(state=SurveyData.num_participants)
    return message.answer("Сколько готовы прийти вместе с тобой?")


@router.message(SurveyData.num_participants, F.text)
async def handle_num_participants(message: types.Message, state: FSMContext):
    """-- Сколько готовы прийти вместе с тобой?"""
    await state.update_data(num_participants=message.text)
    await state.set_state(state=SurveyData.sum_revenue)
    return message.answer("Общий ревенью в месяц. И ревенью на каждого баера.")


@router.message(SurveyData.sum_revenue, F.text)
async def handle_sum_revenue(message: types.Message, state: FSMContext):
    """-- Общий ревенью в месяц. И ревенью на каждого баера"""
    await state.update_data(sum_revenue=message.text)
    await state.set_state(state=SurveyData.your_avg_spend)
    return message.answer("Ваш средний спенд в месяц.")
