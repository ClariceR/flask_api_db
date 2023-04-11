## What do I need to connect to the DB?

- First thing, we need to import the mysql connector
```buildoutcfg
import mysql.connector
```

- Then we need to import the db details we saved in the congif file
```buildoutcfg
from config_db_connection import HOST, USER
```

- We also want create a custom exception in case there is a problem
connceting with the DB.
  > This is very important: we need to make sure we log the error
  > in case an unexpected error occurs and we need to debug our code.
  > Luckly this is incredible easy to do :) This is how you do it:
  > 
*First we import logging:*
```buildoutcfg
import logging
```
*This is our custom exception. Istead of pass, we add a docstring with info
about the custom error*
```buildoutcfg
class DBConnectionError(Exception):
    '''DB connection error'''
```
*Then, inside our except in our try/except block we log the error
as well as raising the exception:*

```buildoutcfg
try:
    ...
except Exception as e:
    logging.exception('Failed to connect to the DB')
    raise DBConnectionError('Failed')
```

## Creating a connection to the DB

- Create a function to connect with the db that takes the db name as a parameter
- Inside we call the function connect from mysql.connection and pass the
db details. We then return the connection.
  
```buildoutcfg
def connect_to_db(db_name):
    connection = mysql.connector.connect(
        host=HOST,
        user=USER,
        database=db_name
    )
    return connection
```

- Next we create the [function to get the records](/docs/getting_all_records.md)

