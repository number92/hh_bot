from app.core.logger import get_logger
from aiogram import Router, types, F
from app.keyboards.menu import MainDataMenu
from app.keyboards.position import kb_choose_position

router = Router(name=__name__)
logger = get_logger(__name__)
