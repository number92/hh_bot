import os
import logging
from datetime import datetime
from app.core import config
from typing import TypeVar

T = TypeVar("T")


def get_logger(
    name=__name__, base_dir=config.BASE_DIR, level=logging.INFO, handler: str = "file"
) -> logging.Logger:

    def _get_log_file_path(base_dir: str) -> str:
        log_dir = os.path.join(base_dir, "logs")
        os.makedirs(log_dir, exist_ok=True)
        return os.path.join(log_dir, f"{datetime.now().strftime('%d-%m-%Y')}.log")

    def _get_handler(handler: str):
        if handler == "file":
            log_file = _get_log_file_path(base_dir)
        return (
            logging.FileHandler(log_file)
            if handler == "file"
            else logging.StreamHandler()
        )

    logger = logging.getLogger(name)
    logger.setLevel(level)
    file_handler = _get_handler(handler)
    file_handler.setLevel(level)

    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    return logger
