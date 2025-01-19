import asyncio
import logging


from app.core import config
from app.core.logger import get_logger
from aiogram.client.bot import DefaultBotProperties
from aiogram import Bot, Dispatcher

# from bot.routers import router as main_router
# from bot.routers.commands.utils import set_default_commands

# Раскоментировать для записи в файл
logger = get_logger(__name__, level=logging.DEBUG, handler=None)

dp = Dispatcher()
# dp.include_router(main_router)
bot = Bot(config.TOKEN, default=DefaultBotProperties(parse_mode="HTML"))


async def main():
    try:
        logger.info("Запуск бота")

        await dp.start_polling(bot)
    except KeyboardInterrupt:
        await dp.stop_polling()
        logger.info("Остановка бота")

    except Exception as e:
        logger.error(e)


if __name__ == "__main__":
    asyncio.run(main())
