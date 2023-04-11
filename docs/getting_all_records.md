## How do we get all the records?

**inside a try/except/finally block:**
- inside the try:
    - define our db name
    - open a connection by calling `connect_to_db` passing the `db_name`
      as argument and saving it in a variable
    - open a cursor, this is what allows us to interact with the DB
      (remember that at the end, we need to close the cursor)
    - write our query
    - tell the cursor to execute the query
    - fetch the result and save them in a variable
    - if you want to see the result, print the items in a for loop
    - close the cursor

- Inside the except:

    - create an exception that will log the error
    - raise the custom exception we created

- Inside the finally:
    - close the connection to the DB

```buildoutcfg
def get_all_records():
    try:
        db_name = 'wishlist_app'
        db_connection = connect_to_db(db_name)
        cursor = db_connection.cursor()
        print('Connected to', db_name)

        query = '''SELECT * FROM wl_items'''
        cursor.execute(query)
        items = cursor.fetchall()
        
        for i in results:
            print(i)

        cursor.close()
        
    except Exception as e:
        logging.exception('Failed to connect to the DB')
        raise DBConnectionError('Failed')
        
    finally:
        if db_connection:
            db_connection.close()
            print('DB connection is closed')
```
