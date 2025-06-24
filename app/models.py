from config import DB_FILEPATH
from sqlalchemy import (
    create_engine,
    Boolean,
    Column,
    DateTime,
    Integer,
    LargeBinary,
    String,
    Text,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(100), unique=True)
    password = Column(LargeBinary)
    firstname = Column(String(100))
    lastname = Column(String(100))
    phonenumber = Column(String(100))
    email = Column(String(100))
    organization = Column(String(100))
    industry = Column(String(100))
    companysize = Column(String(100))
    department = Column(String(100))
    jobrole = Column(String(100))
    city = Column(String(100))
    country = Column(String(100))

    is_activated = Column(Boolean, nullable=False, default=False)
    activation_token = Column(String(100))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())


class Log(Base):
    __tablename__ = "log"
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(100), nullable=False)
    page = Column(String(100), nullable=False)
    session_id = Column(Integer)

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())


ENGINE = create_engine(f"sqlite:///{DB_FILEPATH}")
Base.metadata.create_all(ENGINE)
