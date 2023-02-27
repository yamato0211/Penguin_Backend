from pydantic import BaseModel
from datetime import date
from schemas.menus import Menu

class GetDailyMenu(BaseModel):
    date: date

class InputDailyMenu(BaseModel):
    weight: float
    count: int
    date: date

class DailyMenu(BaseModel):
    id: str
    weight: float
    count: int
    date: date
    menu_id: str
    menu: Menu

    class Config:
        orm_mode = True
