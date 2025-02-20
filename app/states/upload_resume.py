from aiogram.fsm.state import StatesGroup, State


class UploadResume(StatesGroup):
    for_vacancy = State()
    waiting_for_resume = State()
