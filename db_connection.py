import mysql.connector
from config_db_connection import HOST, USER
import logging


class DBConnectionError(Exception):
    '''DB connection error'''


def connect_to_db(db_name):
    connection = mysql.connector.connect(
        host=HOST,
        user=USER,
        # auth_plugin='mysql_native_password',
        database=db_name
    )
    return connection


def get_all_records():
    try:
        db_name = 'wishlist_app'
        db_connection = connect_to_db(db_name)
        cursor = db_connection.cursor()
        print('Connected to', db_name)

        query = '''SELECT * FROM wl_items'''
        cursor.execute(query)
        items = cursor.fetchall()

        # if we want to see it
        for item in items:
            print(item)

        cursor.close()
    except Exception as e:
        logging.exception('Failed to connect to the DB')
        raise DBConnectionError('Failed')
    finally:
        if db_connection:
            db_connection.close()
            print('DB connection is closed')


get_all_records()
