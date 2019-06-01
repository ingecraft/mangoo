from . import db

class Lead(db.Model):
    __tablename__ = 'leads'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    surname = db.Column(db.String(64))
    phone_number = db.Column(db.String(10))
    email = db.Column(db.String(64), unique=True, index=True)

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

    def __repr__(self):
        return '<User %r>' % self.username

class Call(db.Model):
    __tablename__ = 'calls'
    id = db.Column(db.Integer, primary_key=True)
    time_called = db.Column(db.DateTime, index=True)

    def __repr__(self):
        pass

class Callback(db.Model):
    __tablename__ = 'callbacks'
    id = db.Column(db.Integer, primary_key=True)
    active = db.Column(db.Boolean)
    callback_time = db.Column(db.DateTime, index=True)

    def __repr__(self):
        pass

class Success(db.Model):
    __tablename__ = 'successes'
    id = db.Column(db.Integer, primary_key=True)

    def __repr__(self):
        pass
    
class Pass(db.Model):
    __tablename__ = 'passes'
    id = db.Column(db.Integer, primary_key=True)

    def __repr__(self):
        pass

