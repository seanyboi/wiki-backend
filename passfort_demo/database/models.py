# The examples in this file are adjusted and come from the Flask-SQLAlchemy documentation
# For more information please take a look at:
# http://flask-sqlalchemy.pocoo.org/2.1/quickstart/#simple-relationships

from datetime import datetime

from passfort_demo.database import db

class Content(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text)
    pub_date = db.Column(db.DateTime)
    titles_id = db.Column(db.Integer, db.ForeignKey('titles.id'))
    titles = db.relationship('Titles', backref=db.backref('content', lazy='dynamic'))

    def __init__(self, body, titles, pub_date=None):
        self.body = body
        if pub_date is None:
            pub_date = datetime.utcnow()
        self.pub_date = pub_date
        self.titles = titles

    def __repr__(self):
        return '<Content %r>' % self.titles


class Titles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Titles %r>' % self.name
