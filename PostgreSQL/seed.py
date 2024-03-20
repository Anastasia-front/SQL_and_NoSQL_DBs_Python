import psycopg2
from faker import Faker
from psycopg2 import sql

# Launch the PostgreSQL database
'''
via Docker

1. use Terminal
                -> if it does not exist - pull it and run it automatically by command (docker run -it hello-world, for instance)
                -> if it exist - docker run --name some-postgres -p 5432:5432 -e POSTGRES_PASSWORD=mysecretpassword -d postgres

2. open Docker app 
                    -> start 'some-postgres' container
                    -> docker exec -it 8297 (id_container, first numbers) bin/sh ||
                       docker exec -it <name-of-container> /bin/bash
'''

# Connecting to the PostgreSQL database
conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="mysecretpassword",
    host="localhost",
    port="5432",
)


# Creating a cursor
cur = conn.cursor()

# Initializing the random data generator
fake = Faker()

# Filling the users table
for _ in range(7):  # fill in 7 users
    fullName = fake.name()
    email = fake.email()
    cur.execute(
        sql.SQL("INSERT INTO users (fullName, email) VALUES (%s, %s)"),
        (fullName, email),
    )

# Filling the status table
statuses = ["new", "in progress", "completed"]
for status in statuses:
    cur.execute(sql.SQL("INSERT INTO status (name) VALUES (%s)"), (status,))

# Filling the tasks table
for _ in range(10):  # fill in 10 tasks
    title = fake.text(max_nb_chars=50)  # random task title
    description = fake.text()  # random task description
    status_id = fake.random_int(min=1, max=len(statuses))  # random status
    user_id = fake.random_int(min=1, max=7)  # random user
    cur.execute(
        sql.SQL(
            "INSERT INTO tasks (title, description, status_id, user_id) VALUES (%s, %s, %s, %s)"
        ),
        (title, description, status_id, user_id),
    )

# Saving changes to the database
conn.commit()

# Closing the cursor and connecting to the database
cur.close()
conn.close()
