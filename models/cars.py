from .base import Base

class Cars(Base, table=True):
    __tablename__ = "cars"

    name: str
    year: int
    price: int

