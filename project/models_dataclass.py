# coding: utf-8
from typing import Optional
from sqlalchemy import Column, Integer, String, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import registry
from dataclasses import dataclass, field

Base = declarative_base()
metadata = Base.metadata

mapper_registry = registry()


@mapper_registry.mapped
@dataclass
class User:
    __table__ = Table(
        "User",
        mapper_registry.metadata,
        Column("id", Integer, primary_key=True),
        Column("name", String),
        Column("password", String),
    )
    id: int = field(init=False)
    name: Optional[str] = None
    password: Optional[str] = None


# class User(Base):
#     __tablename__ = "User"

#     id = Column(
#         Integer,
#         primary_key=True,
#         server_default=text("nextval('\"User_id_seq\"'::regclass)"),
#     )
#     password = Column(String)
#     name = Column(String)
