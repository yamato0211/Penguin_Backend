from fastapi import APIRouter
from fastapi.params import Depends
from db.db import get_db
from sqlalchemy.orm.session import Session
from service.menus import get_menus, create_menu, update_menu, delete_menu
from schemas.menus import Menu, InputMenuData

menu_router = APIRouter()

@menu_router.get("/", response_model=list[Menu])
async def get_all_menus(db: Session = Depends(get_db)):
    menus = get_menus(db)
    return menus

@menu_router.post("/", response_model=Menu)
async def create_menu_by_details(payload: InputMenuData, db: Session = Depends(get_db)):
    menu = create_menu(
        db=db,
        name=payload.name,
        target=payload.target,
        weight=payload.weight,
        isJoint=payload.isJoint,
        link=payload.link,
    )
    return menu

@menu_router.put("/{id}", response_model=Menu)
async def update_menu_by_details(id: str, payload: InputMenuData, db: Session = Depends(get_db)):
    menu = update_menu(
        db=db,
        id=id,
        name=payload.name,
        target=payload.target,
        weight=payload.weight,
        isJoint=payload.isJoint,
        link=payload.link,
    )

    return menu

@menu_router.delete("/{id}")
async def delete_menu_by_id(id: str, db: Session = Depends(get_db)):
    delete_menu(db=db, id=id)
    return {"message" : "OK!"}