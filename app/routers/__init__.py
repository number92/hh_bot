__all__ = ("router",)

from aiogram import Router
from app.routers.cmds import router as cmd_router
from app.routers.callbacks.buyer import router as buyer_router

router = Router(name=__name__)

router.include_routers(cmd_router, buyer_router)
