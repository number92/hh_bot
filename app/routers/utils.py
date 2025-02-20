import re
from bs4 import BeautifulSoup
from aiogram import types
from typing import Tuple


def format_html_for_telegram(html_text: str, allowed_tags=None) -> str:
    if allowed_tags is None:
        allowed_tags = ["b", "i", "u"]
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

    for tag in soup.find_all(True):
        if tag.name not in ["b", "i", "u"]:
            tag.unwrap()
    formatted_text = str(soup)

    formatted_text = "\n".join(line for line in formatted_text.splitlines())
    formatted_text = re.sub(r"\n\s*\n", "\n", formatted_text)
    return formatted_text


def check_file(document: types.Document) -> Tuple[bool, str]:
    message = ""
    allowed_mime_types = [
        "application/pdf",
        "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        "application/msword",  # Для .doc
        "text/rtf",  # Для .rtf
        "text/plain",  # Для .txt
    ]

    if document.mime_type not in allowed_mime_types:
        message = "Пожалуйста, отправьте резюме в формате PDF, DOC, RTF или TXT."
        return (False, message)

    max_file_size = 5 * 1024 * 1024  # 5 MB
    if document.file_size > max_file_size:
        message = "Файл слишком большой. Пожалуйста, загрузите файл размером не более 5 МБ."
        return (False, message)

    return (True, "")
