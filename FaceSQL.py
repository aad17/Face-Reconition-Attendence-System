import mysql.connector


class FaceSQL:
    def __init__(self):
        self.conn = mysql.connector.connect(
            user='root',
            password='password',
            host='127.0.0.1',
            database='student',
            auth_plugin='mysql_native_password')

    def processFaceData(self, sqlstr, args=()):
        print(sqlstr)
        # Use cursor() method to create a cursor object
        cursor = self.conn.cursor()
        try:
            # Execute sql statement
            cursor.execute(sqlstr, args)
            # Submit to the database to execute
            self.conn.commit()
        except Exception as e:
            # If an error occurs, roll back and print the error message
            self.conn.rollback()
            print(e)
        finally:
            # Close cursor
            cursor.close()

    def saveFaceData(self, rollno, encoding_str):
        self.processFaceData(
            "insert into faces(rollno, face_encoding) values(%s,%s)", (rollno, encoding_str))

    def updateFaceData(self, rollno, encoding_str):
        self.processFaceData(
            "update faces set face_encoding = %s where rollno = %s", (encoding_str, rollno))

    def execute_float_sqlstr(self, sqlstr):
        # Use cursor() method to create a cursor object
        cursor = self.conn.cursor()
        # SQL insert statement

        results = []
        try:
            # Execute sql statement
            cursor.execute(sqlstr)
            # Get a list of all records
            results = cursor.fetchall()
        except Exception as e:
            # If an error occurs, roll back and print the error message
            self.conn.rollback()
            print(e)
        finally:
            # Close cursor
            cursor.close()
        return results

    def sreachFaceData(self, rollno):
        return self.execute_float_sqlstr("select * from faces where student ID="+rollno)

    def allFaceData(self):
        return self.execute_float_sqlstr("select * from faces ")

    def sreach_Info(self, rollno):
        return self.execute_float_sqlstr("select * from student where rollno='" + rollno + "'")
