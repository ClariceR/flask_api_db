## How do I insert a new item in a table?

*We need to create a function and accept the new item as a parameter*
*It will also be structured in the try/ except/ finally blocks*
*Then we start the same way we started when getting the items:*

- create a variable for db name so we can pass it to the connect function
- then we open the connection and save it in a variable
- we also need create the cursor to interact
- then save our query in a variable. 

> Even though the string values in the `new item dict` are strings,
> we still need to add `''` around the value we are getting from the dict
> if, and when, of course our value is VARCHAR (or any other str type)
> 
- then we execute our query
- we then need to commit the changes

> In order to persist the change, we need to commit the changes
> using `db_connection.commit()`
- close the cursor
- The `except` and `finally` blocks are the same as the ones to get
all records.

```buildoutcfg
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
```