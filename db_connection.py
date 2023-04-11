import mysql.connector
from config_db_connection import HOST, USER
import logging


class DBConnectionError(Exception):
    '''DB connection error'''


def _connect_to_db(db_name):
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
        db_connection = _connect_to_db(db_name)
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


new_item = {
    'name': 'Jumper',
    'price': 80.0,
    'link_URL': 'https://www.uniqlo.com/uk/en/product/washable-soft-knit-crew-neck-jumper-454754.html'
}


def insert_record_to_db(new_item):
    try:
        db_name = 'wishlist_app'
        table_name = 'wl_items'
        db_connection = _connect_to_db(db_name)
        cursor = db_connection.cursor()
        print('connected')

        query = f'''INSERT INTO {table_name} (name, price, link_URL)
                    VALUES
                    ('{new_item['name']}', {new_item['price']}, '{new_item['link_URL']}');'''

        cursor.execute(query)
        db_connection.commit()

        cursor.close()
    except Exception as e:
        logging.exception('Failed to connect to the DB')
        raise DBConnectionError('Failed')
    finally:
        if db_connection:
            db_connection.close()
            print('DB connection is closed')


insert_record_to_db(new_item)
get_all_records()
