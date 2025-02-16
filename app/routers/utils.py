from bs4 import BeautifulSoup


def format_html_for_telegram(html_text):
    soup = BeautifulSoup(html_text, "html.parser")
    for strong in soup.find_all("strong"):
        strong.name = "b"

    for p in soup.find_all("p"):
        p.insert_after("\n")
        p.unwrap()

    for ul in soup.find_all("ul"):
        for li in ul.find_all("li"):
            li.insert_before("-  ")
            li.insert_after("\n")
            li.unwrap()
        ul.insert_after("")
        ul.unwrap()
    formatted_text = str(soup)

    formatted_text = "\n".join(line for line in formatted_text.splitlines())
    return formatted_text


# TODO: найти ошибку в форматировании
