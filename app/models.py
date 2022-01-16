from flask_sqlalchemy import SQLAlchemy
from app import app

db = SQLAlchemy(app)

class Patent(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    patent = db.Column(db.String(100), unique=True, nullable=False)
    
    def __repr__(self):
        return '<Patent %r>' % self.patent

db.drop_all()
db.create_all()