import dbcreds
import mariadb

def ask_price():
    price = input("Cars above what price would you like to see?\n")
    return price

def filtering_cars_by_price(car_price):
    try:
        conn = mariadb.connect(password=dbcreds.pasword, user=dbcreds.user, host=dbcreds.host, port=dbcreds.port, database=dbcreds.database)
    except:
        print("Something went wrong. The appropriate person has been notified.")
    cursor = conn.cursor()
    try:
        cursor.execute('CALL filter_by_price(?)', [car_price])
    except mariadb.OperationalError:
        print("You should type only numbers. Please, try again.")
        ask_price()
    except:
        print("Something went wrong. Call for assistance.")
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    for item in result:
        print(item[1], item[2])

conn = mariadb.connect(password=dbcreds.pasword, user=dbcreds.user, host=dbcreds.host, port=dbcreds.port, database=dbcreds.database)
cursor = conn.cursor()
cursor.execute('CALL get_all_items()')
result = cursor.fetchall()
cursor.close()
conn.close()

for item in result:
    print(item[1], item[2])

price = ask_price()
filtering_cars_by_price(price)