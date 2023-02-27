from sqlalchemy.orm.session import Session
from sqlalchemy import desc
from typing import Optional
from db.model import Menu
from schemas.menus import Menu as MenuEntity
from fastapi import HTTPException

def get_menus(db: Session):
    menus_orm = db.query(Menu).order_by(desc(Menu.create_at)).all()
    menus = list(map(MenuEntity.from_orm, menus_orm))
    return menus

def create_menu(db: Session, name: str, target: str, weight: float, isJoint: bool, link: Optional[str]):
    same_menu = db.query(Menu).filter(Menu.name == name).first()
    if same_menu is not None:
        raise HTTPException(status_code=400, detail="same menu is already existed")

    menu_orm = Menu(
        name=name,
        target=target,
        weight=weight,
        isJoint=isJoint,
        link=link,
    )

    db.add(menu_orm)
    db.commit()
    db.refresh(menu_orm)
    menu = MenuEntity.from_orm(menu_orm)
    return menu

def update_menu(db: Session, id: str, name: str, target: str, weight: float, isJoint: bool, link: Optional[str]):
    same_menu = db.query(Menu).filter(Menu.id == id).first()
    if same_menu is None:
        raise HTTPException(status_code=404, detail="menu is not found")
    same_menu.name = name
    same_menu.target = target
    same_menu.weight = weight
    same_menu.isJoint = isJoint
    same_menu.link = link
    db.commit()
    db.refresh(same_menu)

    menu = MenuEntity.from_orm(same_menu)
    return menu

def delete_menu(db: Session, id: str):
    same_menu = db.query(Menu).filter(Menu.id == id).first()
    if same_menu is None:
        raise HTTPException(status_code=404, detail="menu not found")
    db.delete(same_menu)
    db.commit()

    return