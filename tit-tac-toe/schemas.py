import pydantic

class Game(pydantic.BaseModel):
    id: int
    result: str
    finished: bool

    class Config:
        orm_mode = True

class GameCreate(Game):
    pass

