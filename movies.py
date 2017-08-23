import os
import sqlite3
from dbcreate import Table

#print(__file__)
#print (os.path.dirname(__file__))
#print (os.path.abspath(__file__))
#print(os.path.split(__file__))

def create_table():
    db = sqlite3.Connection('dvd.db')
    s = os.path.join()
    s = 'mama'

def create_directors(db):
    ct = """
    CREATE TABLE directors
    (id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
    name TEXT UNIQUE NOT NULL)
    """
    cursor = db.cursor()
    cursor.execute(ct)
    sql = """INSERT INTO directors
          (name)
          VALUES (?)
          """
    cursor.execute(sql,("Direktor Jožko",))
    print("Added one record to table")

        
def create_actors(db):
    tbl_actors = Table("actors")
    tbl_actors.add_field("id", "INTEGER", pk=True, autoinc=True, notnull=True,unique=True)
    tbl_actors.add_field("name","TEXT")
    ssql = tbl_actors.create_sql()
    print(ssql)
    cursor = db.cursor()
    cursor.execute(ssql)
    print("Table actors was created")

def create_actors_dvds(db):
    tbl_dvds = Table("actors_dvds")
    tbl_dvds.add_field("id","INTEGER",pk=True, autoinc="True")
    tbl_dvds.add_field("title","TEXT",notnull=True)
    tbl_dvds.add_field("year","INTEGER",notnull=True)
    tbl_dvds.add_field("duration","INTEGER",notnull=True)
    tbl_dvds.add_field("actor_id","INTEGER",notnull=True)
    tbl_dvds.add_refrence("actor_id","actors")
    ssql = tbl_dvds.create_sql()
    print(ssql)
    cursor = db.cursor()
    cursor.execute(ssql)
    print("Table actors_dvds was created")

def create_persons(db):
    person = Table("persons")
    person.add_field("name","TEXT")
    person.add_field("surname","TEXT")
    person.add_field("yeara_old","INTEGER")
    ssql = person.create_sql()
    cursor = db.cursor()
    cursor.execute(ssql)
    print("Table persons was created")

def connect(filename):
    db = sqlite3.connect(filename)
    return db

def main():
    file_name = os.path.join(os.path.dirname(__file__),"dvds.db")
    db = connect(file_name)
    #create_actors_dvds(db)
    create_persons(db)


if __name__ == "__main__":
    main()

