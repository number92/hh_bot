from app.core.logger import get_logger
from aiogram import Router, types, F

router = Router(name=__name__)
logger = get_logger(__name__)


@router.callback_query(F.text == "back-main")
async def handle_backbtn(callback_query: types.CallbackQuery):
    pass


# TODO : остановился
