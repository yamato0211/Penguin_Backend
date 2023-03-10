from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, Float ,Boolean, Date, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from uuid import uuid4
from datetime import datetime

Base = declarative_base()

def create_uuid():
    return str(uuid4())

class Menu(Base):
    __tablename__ = "menus"
    id = Column(String, primary_key=True, default=create_uuid)
    name = Column(String, unique=True)
    target = Column(String)
    weight = Column(Float)
    isJoint = Column(Boolean)
    link = Column(String, nullable=True)
    create_at = Column(DateTime, default=datetime.now, nullable=True)
    daily_menus = relationship("DailyMenu", back_populates="menu")

class DailyMenu(Base):
    __tablename__ = "daily_menus"
    id = Column(String, primary_key=True, default=create_uuid)
    weight = Column(Float)
    count = Column(Integer)
    date = Column(Date)
    create_at = Column(DateTime, default=datetime.now, nullable=True)
    menu_id = Column(String, ForeignKey("menus.id"))
    menu = relationship("Menu", back_populates="daily_menus")
