from app import db

class Task(db.Model): #db.Model tells Flask this is a special kind of class that connects to the database.
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(20), default="Pending")
