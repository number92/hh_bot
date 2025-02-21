from app.api_hh.entities import Vacancy
from app.routers.utils import format_html_for_telegram
from aiogram import types


def compile_report(data: dict) -> str:
    position = data.get("position")
    other_source = (
        f"\n<i>Пожалуйста, напиши свой источник.</i> {data.get('other_source')}" if data.get("other_source") else ""
    )
    workers = (
        f"<i>Количество человек в команде.{data.get('count_workers')}</i>\n" if data.get("count_workers", "") else ""
    )
    participants = (
        f"<i>Сколько готовы прийти вместе с тобой? {data.get('num_participants')}</i>\n"
        if data.get("num_participants", "")
        else ""
    )
    your = "Ваш" if position == "Team Lead" else "Твой"
    spend = f"<i>{your} средний спенд в месяц? {data.get('your_avg_spend')}</i>\n"
    if revenue := data.get("your_avg_revenue"):
        revenue_str = f"<i>Твой средний ревенью в месяц?</i> {revenue}\n"
    else:
        revenue_str = f"<i>Общий ревенью в месяц. И ревенью на каждого баера.</i> {data.get('sum_revenue')}"

    profit = (
        "<i>Если рассматривать последний квартал, сколько $"
        f"в месяц составлял твой максимальный профит? {data.get('profit')}</i>\n"
    )

    name_user = ""
    if data.get("first_name"):
        name_user = f"{data.get('first_name')} {data.get('last_name')}"
    elif data.get("username"):
        name_user = data.get("username")
    else:
        name_user = data.get("user_id")

    message = [
        "<i>Соискатель:</i>",
        f"<a href='{data.get('profile_link', '#')}'>  {name_user} </a>\n",
        f"<i>Позиция:</i> {position}\n" f"<i>Напиши свое имя:</i> {data.get('name')}\n",
        f"<i>Выбери свой источник:</i> {data.get('name')}{other_source}\n",
        workers,
        participants,
        f"<i>ГЕО, с которыми вы работаете?</i> {data.get('geo')}\n",
        revenue_str,
        spend,
        profit,
    ]
    return "".join(message)


def list_vacancies_view() -> str:
    return (
        "Ниже можно ознакомиться с открытыми вакансиями. "
        "Если вдруг не нашел подходящей позиции, загрузи свое резюме, и мы обязательно его рассмотрим!"
    )


def choose_position_message() -> str:
    return "Выбери должность на которую претендуешь:"


def make_message_vacancy(vacancy: Vacancy) -> str:
    return format_html_for_telegram(vacancy.description)


def message_for_manager_about_resume(message: types.Message, vacancy: Vacancy) -> str:
    user_link = f"<a href='tg://user?id={message.from_user.id}'>"

    if message.from_user.full_name:
        user_link += message.from_user.full_name
    elif message.from_user.username:
        user_link += f"@{message.from_user.username}"
    else:
        user_link += "Неизвестный пользователь"

    user_link += "</a>"

    return f'Резюме от {user_link} на позицию "{vacancy.name}"'
