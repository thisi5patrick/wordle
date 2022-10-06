from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .tables import ScoreboardEntity


class DatabaseUtils:
    _engine = create_engine("sqlite:///database.sqlite")
    Session = sessionmaker(bind=_engine)

    @staticmethod
    def insert_game(**kwargs):
        if not all(key in kwargs for key in ["game_time_seconds", "attempts", "word"]):
            return
        attempts = kwargs["attempts"]
        word = kwargs["word"]
        game_time_seconds = kwargs["game_time_seconds"]

        with DatabaseUtils.Session() as session:
            scoreboard = ScoreboardEntity(game_time_seconds, word, attempts)
            session.add(scoreboard)
            session.commit()
