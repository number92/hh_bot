def compile_report(data: dict):
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

    message = [
        f"<i>Пользователь:</i> {data.get('firstname')} {data.get('lastname')}",
        f"<i>ссылка:</i> {data.get('firstname')} {data.get('lastname')}",
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


def list_vacancies_view():
    return (
        "Ниже можно ознакомиться с открытыми вакансиями. "
        "Если вдруг не нашел подходящей позиции, загрузи свое резюме, и мы обязательно его рассмотрим!"
    )
