from database import db


class Inventory(db.Model):
    __tablename__ = 'inventory'

    id = db.Column(db.Integer, primary_key=True)
    theatre_id = db.Column(db.Integer, db.ForeignKey('theatre.id'), nullable=False)
    show_id = db.Column(db.Integer, db.ForeignKey('show.id'), nullable=False)
    date = db.Column(db.Date, nullable=False)
    start_time = db.Column(db.Time, nullable=False)
    end_time = db.Column(db.Time, nullable=False)
    retail_price = db.Column(db.Float, nullable=False)
    selling_price = db.Column(db.Float, nullable=False)
    is_active = db.Column(db.Boolean, default=True, nullable=False)
    available_seats = db.Column(db.Integer, default=100, nullable=False)

    # Establish relationships with Theatre and Show
    theatre = db.relationship('Theatre', backref=db.backref('inventory', lazy=True))
    show = db.relationship('Show', backref=db.backref('inventory', lazy=True))
    
    def __init__(self, theatre_id, show_id, date, start_time, end_time, retail_price, selling_price, is_active=True, available_seats=100):
        self.theatre_id = theatre_id
        self.show_id = show_id
        self.date = date
        self.start_time = start_time
        self.end_time = end_time
        self.retail_price = retail_price
        self.selling_price = selling_price
        self.is_active = is_active
        self.available_seats=available_seats

    def save(self):
        db.session.add(self)
        db.session.commit()
