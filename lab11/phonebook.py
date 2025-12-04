from db import get_connection
import csv
import os


def insert():
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


def csv(filename):
    """Загрузка контактов из CSV.
    """
    base_dir = os.path.dirname(__file__)
    full_path = os.path.join(base_dir, filename)

    if not os.path.exists(full_path):
        print(f"File '{full_path}' not found")
        return

    conn = get_connection()
    cur = conn.cursor()

    with open(full_path, newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)

        for row in reader:
            cur.execute(
                """
                INSERT INTO phonebook (first_name, last_name, phone)
                VALUES (%s, %s, %s)
                ON CONFLICT (phone)
                DO UPDATE SET
                    first_name = EXCLUDED.first_name,
                    last_name  = EXCLUDED.last_name
                """,
                (row['first_name'], row['last_name'], row['phone'])
            )

    conn.commit()
    cur.close()
    conn.close()

    print("CSV imported-updated")


def upd_number():
    name = input("First name update: ")
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


def search_name():
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


def delete():
    phone = input("Phone delete: ")

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "DELETE FROM phonebook WHERE phone = %s",
        (phone,)
    )

    conn.commit()
    print(f"Deleted: {cur.rowcount}")

    cur.close()
    conn.close()


def pattern():
    pattern = input("Enter pattern: ")

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM find_phonebook(%s)", (pattern,))
    rows = cur.fetchall()

    print("Results:")
    for r in rows:
        print(r)

    cur.close()
    conn.close()


def instert_upd():
    first_name = input("First name: ")
    last_name = input("Last name: ")
    phone = input("Phone: ")

    if last_name.strip() == "":
        last_name = None

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("CALL upsert_phonebook_user(%s, %s, %s)", (first_name, last_name, phone))
    conn.commit()

    cur.close()
    conn.close()

    print("Done")



def bulk_insert():
    n = int(input("How many users to insert: "))

    first_names = []
    last_names = []
    phones = []

    for i in range(n):
        print(f"\nUser #{i+1}:")
        f = input("  First name: ")
        l = input("  Last name: ")
        p = input("  Phone: ")

        if l.strip() == "":
            l = None

        first_names.append(f)
        last_names.append(l)
        phones.append(p)

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "CALL bulk_insert_users(%s, %s, %s)",
        (first_names, last_names, phones)
    )
    conn.commit()

    cur.execute("SELECT first_name, last_name, phone FROM invalid_phones")
    bad_rows = cur.fetchall()

    if bad_rows:
        print("\nIncorrect phones:")
        for r in bad_rows:
            print(r)
    else:
        print("\nSuccessfully.")

    cur.close()
    conn.close()


def show_page():
    limit = int(input("Limit: "))
    offset = int(input("Offset): "))

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM get_phonebook_page(%s, %s)", (limit, offset))
    rows = cur.fetchall()

    print(f"\nPage (limit={limit}, offset={offset}):")
    for r in rows:
        print(r)

    cur.close()
    conn.close()


def delete_user():
    mode = input("Delete (n)ame/(p)hone? ").strip().lower()

    name = None
    phone = None

    if mode == "n":
        name = input("Enter name: ")
    elif mode == "p":
        phone = input("Enter phone: ")
    else:
        print("Wrong")
        return

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("CALL delete_from_phonebook(%s, %s)", (name, phone))
    conn.commit()

    print("Deleted")

    cur.close()
    conn.close()


def menu():
    while True:
        print("\nPHONE BOOK")
        print("1. Insert user")
        print("2. Insert users CSV")
        print("3. Update phone")
        print("4. Search name")
        print("5. Delete phone")
        print("6. Search by pattern")
        print("7. Insert/Update user")
        print("8. Bulk insert users")
        print("9. Show page")
        print("10. Delete via procedure")
        print("0. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            insert()
        elif choice == "2":
            filename = input("Enter CSV: ")
            csv(filename)
        elif choice == "3":
            upd_number()
        elif choice == "4":_name()
        elif choice == "5":
            delete()
        elif choice == "6":
            pattern()
        elif choice == "7":
            instert_upd()
        elif choice == "8":
            bulk_insert()
        elif choice == "9":
            show_page()
        elif choice == "10":
            delete_user()
        elif choice == "0":
            print("CU again")
            break
        else:
            print("Wrong")


if __name__ == "__main__":
    menu()