from pydantic import BaseModel
from typing import Optional
from datetime import date
from datetime import datetime

class InputMenuData(BaseModel):
    name: str
    target: str
    weight: float
    isJoint: bool
    link: Optional[str]


class DailyMenu(BaseModel):
    id: str
    weight: float
    count: int
    date: date
    menu_id: str

    class Config:
        orm_mode = True

class Menu(BaseModel):
    id: str
    name: str
    target: str
    weight: float
    isJoint: bool
    link: str
    create_at: datetime

    class Config:
        orm_mode = True

