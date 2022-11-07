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

def make_move(db: sqlalchemy.orm.Session, game_id: int, move: schemas.Move):
    db_game = db.query(models.Game).filter(models.Game.id == game_id).first()

    if db_game.result[move.position] == '-' and 0 <= move.position <= 8:
        cur_game = list(db_game.result)
        cur_game[move.position] = move.type
        cur_game = ''.join(cur_game)

        db_game.result = cur_game
        db.commit()
        db.refresh(db_game)
        return {"result": "success"}
    else:
        return {"result": "error", "error_code":"invalid_position"}

def check_game(db: sqlalchemy.orm.Session, game_id: int):
    db_game = db.query(models.Game).filter(models.Game.id == game_id).first()
    board = db_game.result

    positions = [[0, 1, 2],
                [3, 4, 5],
                [6, 7, 8],
                [0, 3, 6],
                [1, 4, 7],
                [2, 5, 8],
                [0, 4, 8],
                [2, 4, 6],]

    def check_draw():
        for i in board:
            if board[a] != '-':
                return False
        return True

    for i in positions:
        a, b, c = i
        if board[a] != '-':
            if board[a] == board[b] and board[b] == board[c]:
                winner = board[a]
                db_game.finished = True
                break

    draw = check_draw()
            
    if db_game.finished:
        status = {"game": "finished", "winner": winner if not draw else null}
    else:
        status = {"game": "in_progress"}

    return status

