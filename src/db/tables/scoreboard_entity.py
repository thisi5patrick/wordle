from sqlalchemy import Column
from sqlalchemy.dialects.sqlite import INTEGER, TEXT

from .. import Base


class ScoreboardEntity(Base):
    __tablename__ = "scoreboard"

    id = Column(INTEGER, primary_key=True, autoincrement=True)
    game_time_seconds = Column(INTEGER, nullable=False)
    word = Column(TEXT, nullable=False)
    attempts = Column(INTEGER, nullable=False)

    def __init__(self, game_time_seconds: int, word: str, attempts: int):
        self.game_time_seconds = game_time_seconds
        self.word = word
        self.attempts = attempts
