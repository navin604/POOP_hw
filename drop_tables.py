from database import db
x = db.cursor()
x.execute('DROP TABLE bankaccount')