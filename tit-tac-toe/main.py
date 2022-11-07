from typing import List
import fastapi as fastapi
import sqlalchemy.orm
import services, schemas

app = fastapi.FastAPI()
services.create_database()

@app.post("/games/", response_model=schemas.Game)
def insert_game(
    game: schemas.GameCreate,
    db: sqlalchemy.orm.Session = fastapi.Depends(services.get_db)
):
    return services.insert_game(db=db, game=game)

@app.get("/games/", response_model=List[schemas.Game])
def read_games(
    skip: int = 0, 
    limit: int = 10, 
    db: sqlalchemy.orm.Session = fastapi.Depends(services.get_db),
):
    games = services.get_games(db=db, skip=skip, limit=limit)
    return games
