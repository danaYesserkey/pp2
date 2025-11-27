import psycopg2

def get_connection():
    return psycopg2.connect(
        host="localhost",
        database="lab10",
        user="postgres",
        password="12345"
    )


# cd ~/Desktop/LAB10/phone_book
# python3 phonebook.py

# add:
# 1
# csv:
# 2
# contacts.csv
# upd:
# 3
# find:
# 4
# del:
# 5


# psql -U postgres -d lab10
# SELECT * FROM phonebook;

# psql -U postgres -d lab10
# SELECT * FROM game_user;
# SELECT * FROM user_score;

