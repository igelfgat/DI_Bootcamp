# XP Exercises : SQL Alchemy

## What you will learn 
- Connect to a database using SQLAlchemy
- Reflect an existing database schema
- Execute basic SQL queries using SQLAlchemy
- Utilize SQLAlchemy's ORM capabilities to interact with the database
- Perform data retrieval and manipulation with pandas

## What you will create
You will create SQL queries and Python scripts to interact with the Chinook sample database using SQLAlchemy and pandas. By the end of these exercises, you will be able to fetch, display, and analyze data from the database.


## Dataset
In these exercises, we’re going to experiment with the [Chinook sample DB](https://www.sqlitetutorial.net/wp-content/uploads/2018/03/chinook.zip) while using SQLAlchemy module

First, run the code below to download the database locally

```python
### download and extract chinook sample DB
import urllib.request
import zipfile
from functools import partial
import os

chinook_url = 'http://www.sqlitetutorial.net/wp-content/uploads/2018/03/chinook.zip'
if not os.path.exists('chinook.zip'):
    print('downloading chinook.zip ', end='')
    with urllib.request.urlopen(chinook_url) as response:
        with open('chinook.zip', 'wb') as f:
            for data in iter(partial(response.read, 4*1024), b''):
                print('.', end='', flush=True)
                f.write(data)

zipfile.ZipFile('chinook.zip').extractall()
assert os.path.exists('chinook.db')

```

The helper methods below will help, you may use for the following exercises : 

```python
### useful: functions for displaying results from sql queries using pandas
from IPython.display import display
import pandas as pd

def sql(query):
    print()
    print(query)
    print()

def get_results(query):
    global engine
    q = query.statement if isinstance(query, sqlalchemy.orm.query.Query) else query
    return pd.read_sql(q, engine)

def display_results(query):
    df = get_results(query)
    display(df)
    sql(query)

```


---

## Exercise 1 : Open the database

- open the database using sqlalchemy module interface. create an engine object in a variable named engine
- call the connect() method to obtain a connection and place in a variable named cur

now run the code below to to run reflecton on the database, prepare classes that map to the database and create an orm session : 
```python
### useful: extract classes from the chinook database
metadata = sqlalchemy.MetaData()
metadata.reflect(engine)

## we need to do this once
from sqlalchemy.ext.automap import automap_base

# produce a set of mappings from this MetaData.
Base = automap_base(metadata=metadata)

# calling prepare() just sets up mapped classes and relationships.
Base.prepare()

# also prepare an orm session
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
session = Session()
```

---

## Exercise 2 : table names
- print out all the table names

---

## Exercise 3 : Tracks
- print out the first three tracks in the tracks table

---

## Exercise 4 : Albums from Tracks
- print out the track name and albums title of the first 20 tracks in the tracks table

---

## Exercise 5 : Tracks sold
- print out the first 10 track sales from the invoice_items table
- for these first 10 sales, print what are the names of the track sold, and the quantity sold

---

## Exercise 6 : Top tracks sold
- print the names of top 10 tracks sold, and how many they times they were sold

---

## Exercise 7 : Top selling artists
- Who are the top 10 highest selling artists?

---





