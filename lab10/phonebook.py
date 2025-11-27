from db import get_connection
import csv

def insert_user_console():
    first_name = input("First name: ")
    last_name = input("Last name: ")
    phone = input("Phone: ")

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        INSERT INTO phonebook (first_name, last_name, phone)
        VALUES (%s, %s, %s)
        """,
        (first_name, last_name, phone)
    )

    conn.commit()
    cur.close()
    conn.close()

    print("User added")


def insert_from_csv(filename):
    conn = get_connection()
    cur = conn.cursor()

    with open(filename, newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)

        for row in reader:
            cur.execute(
                """
                INSERT INTO phonebook (first_name, last_name, phone)
                VALUES (%s, %s, %s)
                """,
                (row['first_name'], row['last_name'], row['phone'])
            )

    conn.commit()
    cur.close()
    conn.close()

    print("CSV")


def update_phone_by_name():
    name = input("First name to update: ")
    new_phone = input("New phone: ")

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        UPDATE phonebook
        SET phone = %s
        WHERE first_name = %s
        """,
        (new_phone, name)
    )

    conn.commit()
    print(f"Updated rows: {cur.rowcount}")

    cur.close()
    conn.close()


def search_by_name():
    name = input("Name: ")

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "SELECT * FROM phonebook WHERE first_name = %s",
        (name,)
    )
    rows = cur.fetchall()

    print("Result:")
    for r in rows:
        print(r)

    cur.close()
    conn.close()

def delete_by_phone():
    phone = input("Phone to delete: ")

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "DELETE FROM phonebook WHERE phone = %s",
        (phone,)
    )

    conn.commit()
    print(f"✔ Deleted rows: {cur.rowcount}")

    cur.close()
    conn.close()


def menu():
    while True:
        print("\nPHONE BOOK")
        print("1. Insert user (console)")
        print("2. Insert users from CSV")
        print("3. Update phone")
        print("4. Search by name")
        print("5. Delete by phone")
        print("0. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            insert_user_console()
        elif choice == "2":
            filename = input("Enter CSV filename: ")
            insert_from_csv(filename)
        elif choice == "3":
            update_phone_by_name()
        elif choice == "4":
            search_by_name()
        elif choice == "5":
            delete_by_phone()
        elif choice == "0":
            print("CU")
            break
        else:
            print("Wrong")


if __name__ == "__main__":
    menu()