### How to create the database

- In MySQLWorkbench, open a new tab and type:

```buildoutcfg
CREATE database wishlist_app;
```

- Declare your intention to use that DB:
```buildoutcfg
USE wishlist_app;
```

### How to create the table

- To create a table, we use the `CREATE table` statement, followed by
the name we want to give.
  
- Then we need a pair of `()` and add the columns and their types inside
```buildoutcfg
CREATE table wl_items (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(45) NOT NULL,
    price FLOAT DEFAULT '0',
    link_URL VARCHAR(2048),
    bought BOOL DEFAULT FALSE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
```

### How to add an item to the table

- To add an item we need the ddl `INSERT INTO`
  followed by the table name, table columns inside `()`
  and then ddl VALUES followed by the values in order according
  to the columns inside `()`, separated by commas
  
```buildoutcfg
INSERT INTO wl_items (name, price, link_URL)
    VALUES
    ('Backpack',
    35.0,
    'https://www.vans.co.uk/shop/en-gb/vans-gb/seeker-mini-backpack-vn00033cbql'
    );
```