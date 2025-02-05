from aiogram.fsm.state import StatesGroup, State


class SurveyData(StatesGroup):
    position = State()
    name = State()
    source = State()
    geo = State()
    revenue = State()
    avg_spend = State()
    profit = State()
