import sqlite3
from sqlite3 import Error
from form_collection import get_json


sql_create_cubes_table = """ CREATE TABLE IF NOT EXISTS cubes (
                                    id integer PRIMARY KEY,
                                    firstname text NOT NULL,
                                    lastname text NOT NULL,
                                    title text NOT NULL,
                                    organization text NOT NULL,
                                    email text NOT NULL,
                                    website text NOT NULL,
                                    phone# text NOT NULL,
                                    opportunities text NOT NULL,
                                    time text NOT NULL
                                ); """


def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

