from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship, declarative_base
from datetime import datetime

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False, index=True)
    password = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    # relações
    lists = relationship("List", back_populates="user", cascade="all, delete-orphan")
    ratings = relationship("Rating", back_populates="user", cascade="all, delete-orphan")


class Movie(Base):
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String, nullable=False)
    description = Column(Text)
    release_year = Column(Integer)
    created_at = Column(DateTime, default=datetime.utcnow)

    # relações
    ratings = relationship("Rating", back_populates="movie", cascade="all, delete-orphan")
    list_movies = relationship("ListMovie", back_populates="movie", cascade="all, delete-orphan")


class List(Base):
    __tablename__ = "lists"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, nullable=False)
    description = Column(Text)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))
    created_at = Column(DateTime, default=datetime.utcnow)

    # relações
    user = relationship("User", back_populates="lists")
    list_movies = relationship("ListMovie", back_populates="list", cascade="all, delete-orphan")


class Rating(Base):
    __tablename__ = "ratings"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    rating = Column(Integer, nullable=False)  # ex: 1 a 5
    comment = Column(Text)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))
    movie_id = Column(Integer, ForeignKey("movies.id", ondelete="CASCADE"))
    created_at = Column(DateTime, default=datetime.utcnow)

    # relações
    user = relationship("User", back_populates="ratings")
    movie = relationship("Movie", back_populates="ratings")


class ListMovie(Base):
    __tablename__ = "list_movies"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    list_id = Column(Integer, ForeignKey("lists.id", ondelete="CASCADE"))
    movie_id = Column(Integer, ForeignKey("movies.id", ondelete="CASCADE"))
    created_at = Column(DateTime, default=datetime.utcnow)

    # relações
    list = relationship("List", back_populates="list_movies")
    movie = relationship("Movie", back_populates="list_movies")
