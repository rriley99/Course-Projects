from user import User
from database import Database

Databse.inititalize(user='postgres',
                    password='admin',
                    database='learning',
                    host='localhost')

database_one = Database()
database_two = Database()
