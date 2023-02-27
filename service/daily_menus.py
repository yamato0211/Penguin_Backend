from sqlalchemy.orm.session import Session
from sqlalchemy import desc
from typing import Optional
from db.model import DailyMenu
from schemas.daily_menus import DailyMenu as DailyMenuSchema
from fastapi import HTTPException
from datetime import date

def create_daily_menu(db: Session, menu_id: str, weight: float, count: int, date: date):
    # same_daily_menu = db.query(DailyMenu).filter(DailyMenu.menu_id == menu_id , DailyMenu.date == date).first()
    # if same_daily_menu is not None:
    #     raise HTTPException(status_code=400, detail="this name menu is already existed")
    daily_menu_orm = DailyMenu(
        weight=weight,
        count=count,
        date=date,
        menu_id=menu_id,
    )

    db.add(daily_menu_orm)
    db.commit()
    db.refresh(daily_menu_orm)

    daily_menu = DailyMenuSchema.from_orm(daily_menu_orm)
    return daily_menu

def get_daily_menus(db: Session, date: date):
    daily_menus_orm = db.query(DailyMenu).filter(DailyMenu.date == date).order_by(desc(DailyMenu.create_at)).all()
    daily_menus = list(map(DailyMenuSchema.from_orm, daily_menus_orm))
    return daily_menus

def get_all_daily_menus(db: Session):
    daily_menus_orm = db.query(DailyMenu).order_by(desc(DailyMenu.date)).all()
    daily_menus = list(map(DailyMenuSchema.from_orm, daily_menus_orm))
    return daily_menus

def update_daily_menu(db: Session, id: str, weight: float, count: int, date: date):
    same_daily_menu = db.query(DailyMenu).filter(
        DailyMenu.id == id).first()
    if same_daily_menu is None:
        raise HTTPException(status_code=404, detail="menu not found")
    same_daily_menu.weight = weight
    same_daily_menu.count = count
    same_daily_menu.data = date
    db.add(same_daily_menu)
    db.commit()
    db.refresh(same_daily_menu)

    daily_menu = DailyMenuSchema.from_orm(same_daily_menu)

    return daily_menu

def delete_daily_menu(db: Session, id: str):
    daily_menu = db.query(DailyMenu).filter(DailyMenu.id == id).first()
    if daily_menu is None:
        raise HTTPException(status_code=404, detail="menu not found")
    
    db.delete(daily_menu)
    db.commit()

    return 
