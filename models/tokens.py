from .base import Base
 
class Token(Base, table=True):
    __tablename__ = "tokens"

    access_token: str
    token_type: str