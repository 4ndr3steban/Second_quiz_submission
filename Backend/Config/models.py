from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, String, Integer, Boolean
from typing import List

class Base(DeclarativeBase):
    pass


class Tquery(Base):
    __tablename__ = "tquery"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    date: Mapped[str] = mapped_column(String(11), nullable=False)
    georange: Mapped[str] = mapped_column(String(4), nullable=False)
    country: Mapped[str] = mapped_column(String(255), nullable=True)
    numtop: Mapped[int] = mapped_column(Integer, nullable=False)
    ascentop: Mapped[bool] = mapped_column(Boolean, nullable=False)
    id_pos: Mapped[int] = mapped_column(ForeignKey('tpost.id'), nullable=False)


class Tpost(Base):
    __tablename__ = "tpost"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(String(255), nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    descript: Mapped[str] = mapped_column(String(255), nullable=False)
    _comments: Mapped[List['Tcomment']] = relationship('Tcomment', backref='tpost')
    _query: Mapped["Tquery"] = relationship('Tquery', backref='tpost')


class Tcomment(Base):
    __tablename__ = "tcomment"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    user: Mapped[str] = mapped_column(String(255), nullable=False)
    comment: Mapped[str] = mapped_column(String(255), nullable=False)
    id_post: Mapped[int] = mapped_column(ForeignKey('tpost.id'), nullable=False)