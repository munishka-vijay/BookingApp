from database import db


class Booking(db.Model):

    _tablename_ = 'booking'

    id = db.Column(db.Integer, primary_key=True)
    inventory_id = db.Column(db.Integer, db.ForeignKey('inventory.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    ticket_count = db.Column(db.Integer, nullable=False)
    date = db.Column(db.Date, nullable=False)

    inventory = db.relationship('Inventory', backref=db.backref('booking', lazy=True))
    user = db.relationship('User', backref=db.backref('booking', lazy=True))
    
    
    def _init_(self, inventory_id, user_id, ticket_count, date):
        self.inventory_id = inventory_id
        self.user_id = user_id
        self.ticket_count = ticket_count
        self.date = date

    def save(self):
        db.session.add(self)
        db.session.commit()