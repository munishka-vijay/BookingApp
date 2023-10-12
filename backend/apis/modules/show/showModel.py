from database import db


class Show(db.Model):

    __tablename__ = 'show'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    language = db.Column(db.String(120), nullable=False)
    tag = db.Column(db.String(50), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    
    def __init__(self, name, language, tag, rating):
        self.name = name
        self.language = language
        self.tag = tag
        self.rating = rating

    def save(self):
        db.session.add(self)
        db.session.commit()