from aiogram import F, Router, types
from aiogram.fsm.context import FSMContext

from app.api_hh.hh_client import get_hh_client
from app.keyboards.backbtn import btn_back_to_menu
from app.routers.messages import message_for_manager_about_resume
from app.routers.utils import check_file
from app.states.upload_resume import UploadResume
from app.core.config import TG_MANAGER_ID

router = Router(name=__name__)


@router.message(UploadResume.waiting_for_resume, F.document)
async def handle_resume_upload(message: types.Message, state: FSMContext):
    """Обработчик для загрузки резюме."""
    is_valid, invalid_message = check_file(message.document)
    if not is_valid:
        return await message.answer(invalid_message)

    async with get_hh_client() as hh_api:
        vacancy = await hh_api.get_vacancy(await state.get_value("for_vacancy"))

    await message.bot.send_document(
        chat_id=TG_MANAGER_ID,
        document=message.document.file_id,
        caption=message_for_manager_about_resume(message, vacancy),
    )

    await state.clear()
    return await message.answer(
        text="Спасибо. В течении 1-го рабочего дня мы свяжемся с тобой.", reply_markup=types.ReplyKeyboardRemove()
    )


@router.message(UploadResume.waiting_for_resume)
async def handle_invalid_resume_upload(message: types.Message):
    """Обработчик для случаев, когда пользователь отправляет не файл."""
    await message.answer(
        text="Пожалуйста, отправьте ваше резюме в формате документа. ",
        reply_markup=types.InlineKeyboardMarkup(inline_keyboard=[[btn_back_to_menu()]]),
    )
