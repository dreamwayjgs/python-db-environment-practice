from dataclasses import dataclass
from sqlalchemy import Column, Sequence
from sqlalchemy.orm import registry

mapper_registry = registry()


@mapper_registry.mapped
@dataclass
class User:
    __table__ = Table("User", mapper_registry.metadata, Column("id", Ser))
