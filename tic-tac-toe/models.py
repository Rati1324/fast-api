import sqlalchemy as sql
import sqlalchemy.orm as orm
import database 

class Game(database.Base):
    __tablename__ = "Game"
    id = sql.Column(sql.String, primary_key=True, index=True)
    board = sql.Column(sql.String)
    order = sql.Column(sql.String)
    winner = sql.Column(sql.String)