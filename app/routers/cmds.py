from aiogram import Router, types
from aiogram.filters import CommandStart
from app.keyboards.menu import kb_main_menu

router = Router(name=__name__)


@router.message(CommandStart())
async def handle_start(message: types.Message):
    """Стартовая команда /start"""

    msg = (
        " Приветствую тебя! Мы — <b>Plusteam</b>, команда профессионалов в области медиабаинга,"
        " обладающая пятилетним опытом работы в сферах Performance и Affiliate marketing.Мы "
        "стремительно развиваемся и создаём оптимальные условия для работы в вертикали iGaming."
    )
    await message.answer(msg)
    await message.answer("Выберите подходящий раздел ниже.", reply_markup=kb_main_menu(message))
