"""Seed file to make sample data for db"""

from db import db
from users.models import User
from trades.models import Trade
from app import app

#Create all tables
db.drop_all()
db.create_all()

#Users
user1 = User.signup(username="testuser", email="testuser@mail.com",
                    password="test123", first_name="Test First", last_name="Test Last")

db.session.add(user1)
db.session.commit()
  



from sqlalchemy import inspect

#Function to check if a table exists
def check_table_exists(table_name):
   inspector = inspect(db.engine)
   return table_name in inspector.get_table_names()

#Check if the table 'users' exists
if check_table_exists("users"):
    print("Users table created successfully!")
else:
    print("Users table was not created.")