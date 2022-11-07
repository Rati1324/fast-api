import pydantic

class Game(pydantic.BaseModel):
    id: str
    result: str
    finished: bool

    class Config:
        orm_mode = True

class GameCreate(Game):
    pass

class Move(pydantic.BaseModel):
    type: str
    position: int

    class Config:
        orm_mode = True
