import asyncio
import logging


from app.core import config
from app.core.logger import get_logger
from aiogram.client.bot import DefaultBotProperties
from aiogram import Bot, Dispatcher, types

from app.routers import router as main_router
from aiogram.exceptions import AiogramError, TelegramNetworkError, TelegramServerError


logger = get_logger(__name__, level=logging.DEBUG, handler=None)

dp = Dispatcher()
dp.include_router(main_router)
bot = Bot(config.TOKEN, default=DefaultBotProperties(parse_mode="HTML"))


async def main():
    try:
        logger.info("Запуск бота")
        logging.basicConfig(level=logging.DEBUG)  # Remove

        await bot.set_my_commands([types.BotCommand(command="start", description="Main menu")])

        await dp.start_polling(bot)
    except KeyboardInterrupt:
        await dp.stop_polling()
        logger.info("Остановка бота")

    except (TelegramServerError, TelegramNetworkError):
        await dp.stop_polling()
        await dp.start_polling(bot)
        logger.info("Проблемы подключения к серверу Telegram, перезагрузка бота.")

    except Exception as e:

        logger.error(e)


if __name__ == "__main__":
    asyncio.run(main())
