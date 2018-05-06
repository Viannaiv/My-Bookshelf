﻿from application import db
from application.models import Base

class Author(Base):

    def __init__(self, name):
        self.name = name

AuthorWork = db.Table('AuthorWork',
    db.Column('work_id', db.Integer, db.ForeignKey('work.id'), primary_key=True),
    db.Column('author_id', db.Integer, db.ForeignKey('author.id'), primary_key=True)
)

#Here the methods for searching related works