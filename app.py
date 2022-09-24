from unittest import result
import dbcreds
import mariadb

conn = mariadb.connect(password=dbcreds.pasword, user=dbcreds.user, host=dbcreds.host, port=dbcreds.port, database=dbcreds.database)
cursor = conn.cursor()
cursor.execute('CALL get_all_items')
result = cursor.fetchall()
