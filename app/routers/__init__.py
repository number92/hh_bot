__all__ = ("router",)

from aiogram import Router
from app.routers.cmds import router as cmd_router
from app.routers.callbacks.buyer import router as buyer_router
from app.routers.callbacks.position import router as position_router
from app.routers.callbacks.back import router as back_router
from app.routers.callbacks.survey import router as base_survey_router
from app.routers.surveybase import router as base_dialog_router
from app.routers.surveylead import router as lead_dialog_router

router = Router(name=__name__)

router.include_routers(
    cmd_router,
    buyer_router,
    position_router,
    back_router,
    base_dialog_router,
    base_survey_router,
    lead_dialog_router,
)
