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

        cursor.close()
    except Exception as e:
        logging.exception('Failed to connect to the DB')
        raise DBConnectionError('Failed')


get_all_records()
