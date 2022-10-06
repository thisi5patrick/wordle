from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeMeta

from src.db.tables import *

_engine = create_engine("sqlite:///../../database123.sqlite")

for item in list(globals().values()):
    if isinstance(item, DeclarativeMeta):
        item.__table__.create(_engine)
