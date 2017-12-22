from app import db
class Employee(db.Model):
    """
    Create a Employee Table
    """
    __tablename__ = "employee"

    id = db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String(60) , index=True , unique=True)
    username = db.Column(db.String(60) , index=True , unique=True)
    first_name = db.Column(db.String(60), index=True)
    last_name = db.Column(db.String(60), index=True)

    def __repr__(self):
        return '<Employee: {}>'.format(self.username)