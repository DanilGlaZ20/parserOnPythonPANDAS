host="127.0.0.1"
user="postgres"
password="110875an"
db_name="postgres"


"""from config import host, user, password, db_name

try:
    connection=psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )
    connection.autocommit=True

    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT version();"

        )
        print(f"Server version:{cursor.fetchone()}")
    with connection.cursor() as cursor:
                cursor.execute(
                    """INSERT INTO product(date, sum, shop) VALUES (shoper.text);"""
                )
                print("[INFO] DATA was Succefully inserted")

except Exception as _ex:
             print("[INFO] Error while working with PostgreSQL", _ex)
finally:
            if connection:
                connection.close()
                print("[INFO] PostgreSQL connection closed")"""