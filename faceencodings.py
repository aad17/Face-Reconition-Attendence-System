import mysql.connector
import pickle

conn = mysql.connector.connect(
    user='root',
    password='password',
    host='127.0.0.1',
    database='student',
    auth_plugin='mysql_native_password')
cursor = conn.cursor()

known_face_encodings = []
known_face_names = []

try:
    sql_query = "select rollno from faces"
    cursor.execute(sql_query)
    records = cursor.fetchall()
    for row in records:
        known_face_names.append(str(row))
    sql_query = "select face_encoding from faces where rollno=69"
    cursor.execute(sql_query)
    rows = cursor.fetchall()
    for each in rows:
        # The result is also in a tuple
        for face_stored_pickled_data in each:
            face_data = pickle.loads(face_stored_pickled_data)
            known_face_encodings.append(face_data)
except mysql.connector.error as e:
    print("Error reading data from MySQL table", e)


print(known_face_encodings)
print(known_face_names)
