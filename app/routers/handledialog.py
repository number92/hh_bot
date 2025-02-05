from aiogram import F, Router, types
from aiogram.fsm.context import FSMContext
from app.states.survey import SurveyData

router = Router(name=__name__)


@router.message(SurveyData.name, F.text)
async def handle_write_user_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    return message.answer("")


# TODO: остановился
