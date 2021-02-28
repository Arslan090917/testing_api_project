import datetime

from app import db

class Books(db.Model):
    __tablename__ = 'books'
    Id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String, nullable=False)
    Genre = db.Column(db.String, nullable=False)
    Price = db.Column(db.Integer, nullable=False)
    Count = db.Column(db.Integer, nullable=False)
    Magazine = db.Column(db.String, nullable=False)
    isAvailable = db.Column(db.Boolean, nullable=False)
    CreatedDateUtc = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow())

    def __repr__(self):
        return str({k: v for k, v in self.__dict__.items() if k[0].isupper()})


class Prices(db.Model):
    __tablename__ = 'prices'
    Id = db.Column(db.Integer, primary_key=True)
    Prices = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return str({k: v for k, v in self.__dict__.items() if k[0].isupper()})

class Magazines(db.Model):
    __tablename__ = 'magazines'
    Id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String, nullable=False)

    def __repr__(self):
        return str({k: v for k, v in self.__dict__.items() if k[0].isupper()})