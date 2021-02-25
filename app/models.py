"""
This file is for creating the database tables using sqlalchemy object 'db'
"""

from app.init_app import db, app, ma
from sqlalchemy import ForeignKey, DateTime
from sqlalchemy.engine import Engine
from sqlalchemy import event


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
    password = db.Column(db.String(120), nullable=False)
    user_type = db.Column(db.Integer)   # 0 -> normal user, 1 -> admin

    def __repr__(self):     
        return '<User: id: {0}, email: {1}, password: {2}>'.format(self.id, self.email, self.name)


class Employee(db.Model):
    """
    brief : db table for storing all employees data
    """

    __tablename__ = "employee"
    
    id = db.Column(db.Integer, ForeignKey(User.id), index=True, primary_key=True)
    email = db.Column(db.String(120), nullable=False, unique=True)
    name = db.Column(db.String(120), nullable=False)
    manager_id = db.Column(db.Integer, ForeignKey(User.id), index=True, primary_key=True)

    def __repr__(self):     
        return '<employee: id: {0}, manager_id: {1}>'.format(self.id, self.manager_id)

class LeaveRequest(db.Model):
    """
    brief : db table for storing all employees data
    """

    __tablename__ = "leave_request"
    
    id = db.Column(db.Integer, ForeignKey(User.id), index=True, primary_key=True)
    manager_id = db.Column(db.Integer, ForeignKey(User.id), index=True, primary_key=True)
    leave_date = db.Column(DateTime, nullable=False)

    def __repr__(self):     
        return '<employee: id: {0}, manager_id: {1}>'.format(self.id, self.manager_id)