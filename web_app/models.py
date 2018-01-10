from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, Column, String

db=SQLAlchemy()


class Page(db.Model):
    __tablename__='page'
    id=Column(Integer, primary_key=True)
    title=Column(String)
    tag=Column(String)
    content=Column(String)


class Post(db.Model):
    __tablename__='post'
    id=Column(Integer, primary_key=True)
    content=Column(String)

