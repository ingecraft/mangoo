from . import db

class Lead(db.Model):
    __tablename__ = 'leads'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    surname = db.Column(db.String(64))
    phone_number = db.Column(db.String(10))
    email = db.Column(db.String(64), unique=True, index=True)
    phone_call_id = db.Column(db.Integer, db.ForeignKey('phone_calls.id'))
    phone_call = db.relationship('PhoneCall')

    def __repr__(self):
        return '<Lead %r>' % self.email

class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)

    def __repr__(self):
        return '<Role %r>' % self.name

class Operator(db.Model):
    __tablename__ = 'operators'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    phone_call = db.relationship("PhoneCall", uselist=False, back_populates="operators")

    def __repr__(self):
        return '<User %r>' % self.username

class PhoneCall(db.Model):
    __tablename__ = 'phone_calls'
    id = db.Column(db.Integer, primary_key=True)
    datetime = db.Column(db.DateTime, index=True)
    operator_id = db.Column(db.Integer, db.ForeignKey('operator.id'))
    operator = db.relationship("Operator", back_populates="phone_calls") 


