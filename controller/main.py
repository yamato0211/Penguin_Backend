from fastapi import APIRouter
from controller.menus import menu_router
from controller.daily_menus import daily_menu_router

router = APIRouter()

router.include_router(menu_router, prefix="/menus", tags=["menus"])
router.include_router(daily_menu_router, prefix="/daily", tags=["daily"])