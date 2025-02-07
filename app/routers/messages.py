def compile_report(data: dict):
    position = data.get("position")
    other_source = (
        f"\n<u>Пожалуйста, напиши свой источник.</u> {data.get('other_source')}" if data.get("other_source") else ""
    )
    workers = (
        f"<u>Количество человек в команде.{data.get('count_workers')}</u>\n" if data.get("count_workers", "") else ""
    )
    participants = (
        f"<u>Сколько готовы прийти вместе с тобой?{data.get('num_participants')}</u>\n"
        if data.get("num_participants", "")
        else ""
    )
    your = "Ваш" if position == "Team Lead" else "Твой"
    spend = f"<u>{your} средний спенд в месяц?{data.get('your_avg_spend')}</u>\n"
    if revenue := data.get("your_avg_revenue"):
        revenue_str = f"<u>Твой средний ревенью в месяц?</u> {revenue}\n"
    else:
        revenue_str = f"<u>Общий ревенью в месяц. И ревенью на каждого баера.</u> {data.get('sum_revenue')}"
    message = [
        f"<u>Позиция:</u> {position}\n" f"<u>Напиши свое имя:</u> {data.get('name')}\n",
        f"<u>Выбери свой источник:</u> {data.get('name')}{other_source}\n",
        workers,
        participants,
        f"<u>ГЕО, с которыми вы работаете?</u> {data.get('geo')}\n",
        revenue_str,
        spend,
        f"<u>Если рассматривать последний квартал, сколько $ в месяц составлял твой максимальный профит? {data.get('profit')}</u>\n",
    ]
    return "".join(message)
