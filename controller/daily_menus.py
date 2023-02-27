from fastapi import APIRouter
from fastapi.params import Depends
from db.db import get_db
from sqlalchemy.orm.session import Session
from service.daily_menus import get_daily_menus, create_daily_menu, update_daily_menu, delete_daily_menu
from schemas.daily_menus import DailyMenu, InputDailyMenu, GetDailyMenu
from datetime import date

daily_menu_router = APIRouter()

@daily_menu_router.get("/", response_model=list[DailyMenu])
async def get_daily_menus_by_date(date: date, db: Session = Depends(get_db)):
    menus = get_daily_menus(db=db, date=date)
    return menus

# @daily_menu_router.post("/{menu_id}", response_model=DailyMenu)
# async def create_daily_menus_by_detail(menu_id: str, payload: InputDailyMenu, db: Session = Depends(get_db)):
#     menu = create_daily_menu(
#         db=db,
#         menu_id=menu_id,
#         weight=payload.weight,
#         count=payload.count,
#         date=payload.date,
#     )

#     return menu


@daily_menu_router.post("/", response_model=list[DailyMenu])
async def create_many_daily_manus_by_detail(payloads: list[InputDailyMenu], db: Session = Depends(get_db)):
    menus = []
    for payload in payloads:
        menu = create_daily_menu(
            db=db,
            menu_id=payload.menu_id,
            weight=payload.weight,
            count=payload.count,
            date=payload.date
        )
        menus.append(menu)
    
    return menus

@daily_menu_router.put("/{id}", response_model=DailyMenu)
async def update_daily_menu_by_detail(id: str, payload: InputDailyMenu, db: Session = Depends(get_db)):
    menu = update_daily_menu(
        db=db,
        id=id,
        weight=payload.weight,
        count=payload.count,
        date=payload.date
    )
    return menu

@daily_menu_router.delete("/{id}")
async def delete_daily_menu_by_id(id: str, db: Session = Depends(get_db)):
    delete_daily_menu(db=db, id=id)
    return {"message" : "OK!!"}


