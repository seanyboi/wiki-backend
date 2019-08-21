from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def reset_database():
    from passfort_demo.database.models import Content, Titles  # noqa
    db.drop_all()
    db.create_all()
