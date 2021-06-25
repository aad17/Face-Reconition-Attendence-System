import mysql.connector
import datetime

conn = mysql.connector.connect(
    user='root',
    password='password',
    host='127.0.0.1',
    database='student',
    auth_plugin='mysql_native_password')
cursor = conn.cursor()

x = datetime.datetime.now()
x = x.date()
sql = (
    "INSERT INTO attendence(attend, s_id, attend_date)"
    "VALUES(%s, %s, %s);"
)
verify = (
    "SELECT * FROM student WHERE rollno=%s and date=%s"
)
data = (1, 1, x)
data2 = (69, x)

# try:
#     cursor.callproc('attendence_procedure2', ('69'))
#     conn.commit()
#     print("Sucessful")
# except:
#     conn.rollback()
#     print('Unsucessful')
# conn.close()
try:
    cursor.execute(sql, data)
    conn.commit()
    print('Data Inserted')
    print("Successful")
except:
    conn.rollback()
    print('Unsuccessful')
conn.close()
