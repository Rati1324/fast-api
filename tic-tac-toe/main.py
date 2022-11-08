import fastapi as fastapi
import sqlalchemy.orm
from typing import List
import uuid
import services, schemas

app = fastapi.FastAPI()
services.create_database()

@app.get("/start")
def start_game(db: sqlalchemy.orm.Session = fastapi.Depends(services.get_db)):
    new_game = schemas.Game(id=str(uuid.uuid4()), board="---------", order="000000000", winner="null")
    return services.insert_game(db=db, game=new_game)

@app.post("/move/{game_id}")
def move(
    game_id: str,
    move: schemas.Move,
    db: sqlalchemy.orm.Session = fastapi.Depends(services.get_db)
):
    return services.make_move(db, game_id, move)

@app.get("/check/{game_id}")
def check(
    game_id: str,
    db: sqlalchemy.orm.Session = fastapi.Depends(services.get_db)
):
    db_game = services.check(db, game_id)
    return db_game

@app.get("/history")
def history(
    db: sqlalchemy.orm.Session = fastapi.Depends(services.get_db)
):
    return services.get_history(db=db)


