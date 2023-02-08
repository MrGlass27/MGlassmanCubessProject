import sqlite3
from sqlite3 import Error
from form_collection import get_json


sql_create_cubes_table = """ CREATE TABLE IF NOT EXISTS cubes_table (
                                    id integer PRIMARY KEY,
                                    firstname text NOT NULL,
                                    lastname text NOT NULL,
                                    title text NOT NULL,
                                    organization text NOT NULL,
                                    email text NOT NULL,
                                    website text NOT NULL,
                                    phone# text NOT NULL,
                                    opportunities text NOT NULL,
                                    time text NOT NULL,
                                    permission text NOT NULL
                                ); """


def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def push_to_table(info, cursor):
    for record in info:
        work_opportunities = record.get('Field109', None) + " " + record.get('Field110', None) + " " + \
            record.get('Field111', None) + " " + record.get('Field112', None) + " " + \
            record.get('Field113', None) + " " + record.get('Field114', None) + " " + \
            record.get('Field115', None)

        time_period = record.get('Field209', None) + " " + record.get('Field210', None) + " " + \
            record.get('Field211', None) + " " + record.get('Field212', None) + " " + \
            record.get('Field213', None)

        cursor.execute('''INSERT INTO cubes_table VALUES(?,?,?,?,?,?,?,?,?,?,?)''',
                       (record.get('EntryID', None),
                        record.get('Field1', None),
                        record.get('Field2', None),
                        record.get('Field104', None),
                        record.get('Field105', None),
                        record.get('Field106', None),
                        record.get('Field107', None),
                        record.get('Field108', None),
                        work_opportunities,
                        time_period,
                        record.get('Field309', None)))

def db_setup():
