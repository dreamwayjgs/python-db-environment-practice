# coding: utf-8
from sqlalchemy import Column, Integer, String, text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class User(Base):
    __tablename__ = "User"

    id = Column(
        Integer,
        primary_key=True,
        server_default=text("nextval('\"User_id_seq\"'::regclass)"),
    )
    password = Column(String)
    name = Column(String)
