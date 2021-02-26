"""
This file is for creating the database tables using sqlalchemy object 'db'
"""

from app.init_app import db, app, ma
from sqlalchemy import ForeignKey, DateTime
from sqlalchemy.engine import Engine
from sqlalchemy import event
from werkzeug.security import generate_password_hash, check_password_hash


# Enabling foreign keys, sometimes it set to be OFF by default
@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()

#-------------------
# Defining db schema
#-------------------

class User(db.Model):
    """
    brief : db table for storing all users registered on the system
    """

    __tablename__ = "user"
    
    id = db.Column(db.Integer, unique=True, index=True, nullable=False, primary_key=True)
    email = db.Column(db.String(120), nullable=False, unique=True)
    name = db.Column(db.String(120), nullable=False)
    password_hash = db.Column(db.String(120), nullable=False)
    type = db.Column(db.Integer)   # 0 -> normal user, 1 -> admin

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):     
        return '<User: id: {0}, email: {1}>'.format(self.id, self.email)


class Employee(db.Model):
    """
    brief : db table for storing all employees data
    """

    __tablename__ = "employee"
    
    id = db.Column(db.Integer, ForeignKey(User.id, ondelete='CASCADE'), index=True, primary_key=True)
    email = db.Column(db.String(120), ForeignKey(User.email, ondelete='CASCADE'), nullable=False, unique=True)
    manager_id = db.Column(db.Integer, ForeignKey(User.id, ondelete='CASCADE'), index=True, primary_key=True)

    def __repr__(self):     
        return '<employee: id: {0}, manager_id: {1}>'.format(self.id, self.manager_id)

class LeaveRequest(db.Model):
    """
    brief : db table for storing all employees data
    """

    __tablename__ = "leave_request"
    
    id = db.Column(db.Integer, unique=True, index=True, nullable=False, primary_key=True)
    employee_id = db.Column(db.Integer, ForeignKey(User.id, ondelete='CASCADE'), nullable=False)
    manager_id = db.Column(db.Integer, ForeignKey(User.id, ondelete='CASCADE'), nullable=False)
    reason = db.Column(db.String(120), nullable=False)
    request_date = db.Column(DateTime, nullable=False)
    status = db.Column(db.Integer, nullable=False)  # 0 -> unanswered, 1 -> Declined, 2 -> Approved

    def __repr__(self):     
        return '<employee: id: {0}, manager_id: {1}>'.format(self.id, self.manager_id)


#------------------------------------------------------------------------------
# The following is to map result queries to json later using flask_marshamallow
#------------------------------------------------------------------------------

class LeaveRequestSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = LeaveRequest