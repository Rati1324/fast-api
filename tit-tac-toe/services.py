import database, models, schemas
import sqlalchemy.orm

def create_database():
    return database.Base.metadata.create_all(bind=database.engine)

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_games(db: sqlalchemy.orm.Session, skip: int = 0, limit: int = 10):
    return db.query(models.Game).offset(skip).limit(limit).all()

def insert_game(db: sqlalchemy.orm.Session, game: schemas.GameCreate):
    db_game = models.Game(**game.dict())
    db.add(db_game)
    db.commit()
    db.refresh(db_game)
    return db_game.id
    # return db_game

def find_game(db: sqlalchemy.orm.Session, game_id: int, move: schemas.Move):
    db_game = db.query(models.Game).filter(models.Game.id == game_id).first()

    cur_game = list(db_game.result)
    cur_game[move.position] = move.type
    cur_game = ' '.join(cur_game)

    db_game.result = cur_game
    db.commit()
    db.refresh(db_game)
    return db_game
