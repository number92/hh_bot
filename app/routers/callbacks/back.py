from app.core.logger import get_logger
from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext

from app.keyboards.menu import kb_main_menu

router = Router(name=__name__)
logger = get_logger(__name__)


@router.callback_query(F.data == "back-main")
async def handle_backbtn(callback_query: types.CallbackQuery, state: FSMContext):
    await state.clear()
    return await callback_query.message.edit_text(
        "Выберите подходящий раздел ниже.", reply_markup=kb_main_menu(callback_query.message)
    )


# TODO: проверить логику
