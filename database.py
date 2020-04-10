from peewee import SqliteDatabase

db = SqliteDatabase("bank.db")
db.connect()
