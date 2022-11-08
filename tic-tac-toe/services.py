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

def make_move(db: sqlalchemy.orm.Session, game_id: str, move: schemas.Move):
    db_game = db.query(models.Game).filter(models.Game.id == game_id).first()

    last_play = max([int(i) for i in db_game.order])

    if check_game(db_game.board)["game"] != "finished":
        if db_game.board[move.position] == '-' and 0 <= move.position <= 8:
            cur_game = list(db_game.board)
            cur_game[move.position] = move.type
            db_game.board = ''.join(cur_game)

            cur_order = list(db_game.order)
            cur_order[move.position] = str(last_play+1)
            db_game.order = ''.join(cur_order)

            db.commit()
            db.refresh(db_game)
            result = {"result": "success"}
        else:
            result = {"result": "error", "error_code":"invalid_position"}
    else: 
        db_game.finished = True
        db.commit()
        db.refresh(db_game)
        result = {"result": "error", "error_code":"game_is_finished"}
    return result

def check(db: sqlalchemy.orm.Session, game_id: str):
    db_game =  db.query(models.Game).filter(models.Game.id == game_id).first()
    return check_game(db_game.board)


def check_game(board):
    positions = [[0, 1, 2],
                [3, 4, 5],
                [6, 7, 8],
                [0, 3, 6],
                [1, 4, 7],
                [2, 5, 8],
                [0, 4, 8],
                [2, 4, 6],]

    draw = True
    finished = False
    for i in positions:
        a, b, c = i
        if board[a] != '-':
            if board[a] == board[b] and board[b] == board[c]:
                winner = board[a]
                finished = True
                break
        else:
            draw = False
            
    if finished:
        status = {"game": "finished", "winner": winner if not draw else "null"}
    else:
        status = {"game": "in_progress"}

    return status

def get_history(db: sqlalchemy.orm.Session):
    db_games =  db.query(models.Game).all()
    orders = [game.order for game in db_games]

    history = []

    for i in range(len(db_games)):
        history.append({"id": db_games[i].id})
        cur_order = db_games[i].order
        history[i]["history"] = [None]*9

        for j in range(len(cur_order)):
            if cur_order[j] != "0":
                history[i]["history"][int(cur_order[j])-1] = {"position": j, "player": db_games[i].board[j]}
        history[i]["history"] = [i for i in history[i]["history"] if i != None]

    return history
