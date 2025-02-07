from aiogram.fsm.state import StatesGroup, State


class SurveyData(StatesGroup):
    position = State()
    name = State()
    source = State()
    other_source = State()
    geo = State()
    count_workers = State()
    num_participants = State()
    sum_revenue = State()
    your_avg_revenue = State()
    your_avg_spend = State()
    profit = State()
