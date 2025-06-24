from config import DB_FILEPATH
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.pool import NullPool

ENGINE = create_engine(
    f"sqlite:///{DB_FILEPATH}",
    connect_args={"check_same_thread": False},
    poolclass=NullPool,
)
connection = ENGINE.connect()
Session = sessionmaker(ENGINE)
