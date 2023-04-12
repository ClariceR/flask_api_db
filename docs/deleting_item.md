## How to delete an item form a table?

*We start the same way as the function to get items and add item.
This time we'll need to pass the id of the item we want to delete*

*We will need the try/except/finally blocks*

*Inside the try block we open a connection with the database, initialize a cursor,
create a query, execute the query, commit the changes and close the cursor*

*Then we only need to write the except and finally blocks exactly the
same as the previous functions*

```buildoutcfg
def delete_item(id):
    try:
        db_name = 'wishlist_app'
        table_name = 'wl_items'
        db_connection = _connect_to_db(db_name)
        cursor = db_connection.cursor()

        query = f'''DELETE FROM {table_name}
                    WHERE id = {id}'''

        cursor.execute(query)
        db_connection.commit()

        cursor.close()
    except Exception:
        logging.exception('Failed to connect to the DB')
        raise DBConnectionError('Failed')
    finally:
        if db_connection:
            db_connection.close()
            print('DB connection closed')
```