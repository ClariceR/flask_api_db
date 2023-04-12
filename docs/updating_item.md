## How do I insert a new item in a table?

*We need to create a function and accept the updated item as a parameter*
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
- The `except` and `finally` blocks are the same as the get
  all records function.