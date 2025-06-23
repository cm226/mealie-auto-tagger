from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import ForeignKey
from sqlalchemy import String

class Base(DeclarativeBase):
    pass

class Label(Base):
    __tablename__ = "labels"
    id: Mapped[str] = mapped_column(primary_key=True)

class ListItem(Base):
    __tablename__ = "listItems"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    label: Mapped[str] = mapped_column(ForeignKey("labels.id"))
