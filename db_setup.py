import sqlite3
from sqlite3 import Error
from form_collection import get_json


sql_create_cubes_table = """ CREATE TABLE IF NOT EXISTS cubes_table (
                                    id integer,
                                    firstname text NOT NULL,
                                    lastname text NOT NULL,
                                    title text,
                                    organization text NOT NULL,
                                    email text NOT NULL,
                                    website text,
                                    phone# text,
                                    opportunities text,
                                    time text,
                                    permission text
                                ); """


def create_table(cursor, create_table_sql):
    try:
        cursor.execute(create_table_sql)
    except Error as e:
        print(e)
    finally:
        cursor.execute('''DELETE FROM cubes_table''')


def push_to_table(info, cursor):
    for entry in info:
        work_opportunities = entry.get('Field109', None) + " " + entry.get('Field110', None) + " " + \
            entry.get('Field111', None) + " " + entry.get('Field112', None) + " " + \
            entry.get('Field113', None) + " " + entry.get('Field114', None) + " " + \
            entry.get('Field115', None)

        time_period = entry.get('Field209', None) + " " + entry.get('Field210', None) + " " + \
            entry.get('Field211', None) + " " + entry.get('Field212', None) + " " + \
            entry.get('Field213', None)

        cursor.execute('''INSERT INTO cubes_table VALUES(?,?,?,?,?,?,?,?,?,?,?)''',
                       (entry.get('EntryID', None),
                        entry.get('Field1', None),
                        entry.get('Field2', None),
                        entry.get('Field104', None),
                        entry.get('Field105', None),
                        entry.get('Field106', None),
                        entry.get('Field107', None),
                        entry.get('Field108', None),
                        work_opportunities,
                        time_period,
                        entry.get('Field309', None)))


def database_setup():
    json_response = get_json()
    json_response = json_response['Entries']
    connection = None

    try:
        name = 'cubes_database.db'
        connection = sqlite3.connect(name)
        cursor = connection.cursor()
        create_table(cursor, sql_create_cubes_table)
        push_to_table(json_response, cursor)
        connection.commit()
        cursor.close()
    except Error as e:
        print(f'A Database Error has occurred: {e}')
    finally:
        if connection:
            connection.close()
            print('Database connection closed.')
    return json_response


database_setup()
