from app.core.logger import get_logger
from aiogram import Router, types, F
from app.keyboards.menu import MainDataMenu
from app.keyboards.position import kb_choose_position

router = Router(name=__name__)
logger = get_logger(__name__)


@router.callback_query(MainDataMenu.filter(F.slug == "buyer-teamlead"))
async def handle_buyer(callback_query: types.CallbackQuery, callback_data: MainDataMenu):
    """
    Обработка кнопки  я медиабайер/лид
    """
    await callback_query.message.edit_text(text="Выберите позицию:", reply_markup=kb_choose_position())
