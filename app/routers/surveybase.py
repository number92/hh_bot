from aiogram import F, Router, types
from aiogram.fsm.context import FSMContext
from app.core import config
from app.keyboards.position import Position
from app.keyboards.source_work import kb_choose_your_source
from app.routers.messages import compile_report
from app.states.survey import SurveyData

router = Router(name=__name__)


@router.message(SurveyData.name, F.text)
async def handle_write_user_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(state=None)
    return await message.answer("Выбери свой источник:", reply_markup=kb_choose_your_source())


@router.message(SurveyData.source, F.text)
async def handle_source(message: types.Message, state: FSMContext):
    """Ответ на Выбери свой источник: Facebook"""
    await state.update_data(source=message.text)
    await state.set_state(state=SurveyData.geo)
    return await message.answer("ГЕО, с которыми вы работаете?")


@router.message(SurveyData.other_source, F.text)
async def handle_other_source(message: types.Message, state: FSMContext):
    """
    -- Выбери свой источник:
        - Другой
    -- Пожалуйста, напиши свой источник
    """
    await state.update_data(other_source=message.text)
    await state.set_state(state=SurveyData.geo)
    return await message.answer("ГЕО, с которыми вы работаете?")


@router.message(SurveyData.geo, F.text)
async def handle_geo(message: types.Message, state: FSMContext):
    """
    -- С Каким ГЕО вы работаете?
    """
    await state.update_data(geo=message.text)
    position = await state.get_value("position")
    if position == Position.LEAD:
        await state.set_state(SurveyData.count_workers)
        return message.answer(text="Количество человек в команде")

    await state.set_state(state=SurveyData.your_avg_revenue)
    return message.answer("Твой средний ревенью в месяц?")


@router.message(SurveyData.your_avg_revenue, F.text)
async def handle_your_avg_revenue(message: types.Message, state: FSMContext):
    """-- Твой средний ревенью в месяц?"""
    await state.update_data(your_avg_revenue=message.text)
    await state.set_state(state=SurveyData.your_avg_spend)
    return await message.answer("Твой средний спенд в месяц?")


@router.message(SurveyData.your_avg_spend, F.text)
async def handle_your_avg_spend(message: types.Message, state: FSMContext):
    """-- Твой средний спенд в месяц?/ -- Ваш средний спенд в месяц."""
    await state.update_data(your_avg_spend=message.text)
    await state.set_state(state=SurveyData.profit)
    return await message.answer(
        "Если рассматривать последний квартал, сколько $ в месяц составлял твой максимальный профит?"
    )


@router.message(SurveyData.profit, F.text)
async def handle_your_profit(message: types.Message, state: FSMContext):
    """-- Если рассматривать твой последний квартал, сколько $ в месяц составляет твой максимальный профит?"""
    username = message.from_user.username
    user = {
        "first_name": message.from_user.first_name,
        "last_name": message.from_user.last_name,
        "profile_link": f"https://t.me/{username}" if username else "Пользователь не имеет username",
    }
    await state.update_data(profit=message.text)
    data = await state.get_data()
    data.update(user)
    await message.bot.send_message(chat_id=config.TG_MANAGER_ID, text=compile_report(data))
    await state.clear()
    return await message.answer("Спасибо за ответы. В течении 1-го рабочего дня мы свяжемся с тобой. ")
