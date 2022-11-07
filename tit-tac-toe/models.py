import sqlalchemy as sql
import sqlalchemy.orm as orm
import database 

class Game(database.Base):
    __tablename__ = "Game"
    id = sql.Column(sql.Integer, primary_key=True, index=True)
    result = sql.Column(sql.String)
    finished = sql.Column(sql.Boolean)