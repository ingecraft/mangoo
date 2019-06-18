from . import db

class Lead(db.Model):
    __tablename__ = 'leads'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    surname = db.Column(db.String(64))
    phone_number = db.Column(db.String(10))
    email = db.Column(db.String(64), unique=True, index=True)
    calls = db.relationship("Call", backref='lead')
    callbacks = db.relationship("Callback", backref='lead')
    donations = db.relationship("Donation", backref='donor')
    passes = db.relationship("Pass", backref='passer')


    def __repr__(self):
        return '<Lead %r>' % self.email
    

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    email = db.Column(db.String(64), unique=True)
    name = db.Column(db.String(64))
    surname = db.Column(db.String(64)) 
    password = db.Column(db.String(64))
    calls = db.relationship("Call", backref='user')
    callbacks = db.relationship("Callback", backref='creator')
    donations = db.relationship("Donation", backref='owner')
    passes = db.relationship("Pass", backref='owner')

    def __repr__(self):
        return '<User %r>' % self.username


class Call(db.Model):
    __tablename__ = 'calls'
    id = db.Column(db.Integer, primary_key=True)
    call_datetime = db.Column(db.DateTime, index=True)
    call_outcome_id = db.Column(db.Integer, db.ForeignKey('call_outcomes.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    lead_id = db.Column(db.Integer, db.ForeignKey('leads.id'))

    def __repr__(self):
        pass

class CallOutcome(db.Model):
    __tablename__ = 'call_outcomes'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(128))
    abbreviation = db.Column(db.String(8))
    calls = db.relationship("Call", backref='outcome')

class Callback(db.Model):
    __tablename__ = 'callbacks'
    id = db.Column(db.Integer, primary_key=True)
    active = db.Column(db.Boolean)
    callback_time = db.Column(db.DateTime, index=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    lead_id = db.Column(db.Integer, db.ForeignKey('leads.id'))
    
    def __repr__(self):
        pass


class Donation(db.Model):
    __tablename__ = 'donations'
    id = db.Column(db.Integer, primary_key=True)
    # frequency = db.Column(db.Enum)
    amount = db.Column(db.Integer)
    # payment_type = db.Column(db.Enum)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id')) 
    lead_id = db.Column(db.Integer, db.ForeignKey('leads.id')) 

    def __repr__(self):
        pass
    

class Pass(db.Model):
    __tablename__ = 'passes'
    id = db.Column(db.Integer, primary_key=True)
    # reason = db.Column(db.Enum)   
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    lead_id = db.Column(db.Integer, db.ForeignKey('leads.id')) 

    def __repr__(self):
        pass
