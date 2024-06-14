from .base import Base
from sqlmodel import Field

class People(Base, table=True):
    __tablename__ = "people"

    name: str
    car_id: int | None = Field(default=None, foreign_key='cars.id')
