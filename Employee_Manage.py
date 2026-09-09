import mysql.connector
from datetime import datetime
class DBConnect:
    def get_Connection(self):
        try:
            self.connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Amrithasuku@123",
                database="companydb"
            )
            return self.connection
        except Exception as e:
            print(e)
class EmployeeManager(DBConnect):
    def get(self):
        try:
            self.connect = super().get_Connection()
            self.cursor = self.connect.cursor()
            query = "SELECT * FROM employee"
            self.cursor.execute(query)
            records = self.cursor.fetchall()
            print(records)
        except Exception as e:
            print(e)
    def post(self, **kwargs):
        try:
            self.connect = super().get_Connection()
            self.cursor = self.connect.cursor()
            query = """
                insert into employee
                (name, place, mobile, email, department, salary, joining_date)
                values (%s, %s, %s, %s, %s, %s, %s)
            """
            values = [v for v in kwargs.values()]
            self.cursor.execute(query, values)
            self.connect.commit()
            print("Employee added successfully")
        except Exception as e:
            print(e)
    def retrieve(self, id):
        try:
            self.connect = super().get_Connection()
            self.cursor = self.connect.cursor()
            query = "SELECT * FROM employee WHERE id = %s"
            values = (id,)
            self.cursor.execute(query, values)
            record = self.cursor.fetchone()
            if record == None:
                print("Employee not found")
            else:
                print(record)
        except Exception as e:
            print(e)
    def get_object(self, id=None):
        self.connect = super().get_Connection()
        self.cursor = self.connect.cursor()
        query = "SELECT * FROM employee WHERE id = %s"
        values = (id,)
        self.cursor.execute(query, values)
        record = self.cursor.fetchone()
        return record
    def put(self, id=None, **kwargs):
        try:
            record = self.get_object(id=id)
            if record != None:
                self.cursor = self.connect.cursor()
                placeholder = ""
                for k in kwargs:
                    placeholder += k + "=%s, "
                placeholder = placeholder.rstrip(" ,")
                query = f"update employee SET {placeholder} WHERE id = %s"
                values = [v for v in kwargs.values()]
                values.append(id)
                self.cursor.execute(query, values)
                self.connect.commit()
                print("Employee details updated successfully")
            else:
                print("Employee not found")
        except Exception as e:
            print(e)
    def delete(self, id=None):
        try:
            self.connect = super().get_Connection()
            self.cursor = self.connect.cursor()
            query = "SELECT * FROM employee WHERE id = %s"
            values = (id,)
            self.cursor.execute(query, values)
            record = self.cursor.fetchone()
            if record != None:
                query = "DELETE FROM employee WHERE id = %s"
                self.cursor.execute(query, values)
                self.connect.commit()
                print("Employee deleted successfully")
            else:
                print("Employee not found")
        except Exception as e:
            print(e)
employee_instance = DBConnect()
print(employee_instance.get_Connection())
employee_instance = EmployeeManager()

# employee_instance.post(
#     name="Alan",
#     place="Idukki",
#     mobile="9876543210",
#     email="alan@gmail.com",
#     department="Sales",
#     salary=25000,
#     joining_date=datetime.today()
# )


# employee_instance.post(
#     name="Arjun",
#     place="Ernakulam",
#     mobile="9876543214",
#     email="arjun@gmail.com",
#     department="Marketing",
#     salary=28000,
#     joining_date=datetime.today()
# )


# employee_instance.post(
#     name="Meera",
#     place="Alappuzha",
#     mobile="9876543213",
#     email="meera@gmail.com",
#     department="Finance",
#     salary=32000,
#     joining_date=datetime.today()
# )


# employee_instance.post(
#     name="Rahul",
#     place="Kottayam",
#     mobile="9876543212",
#     email="rahul@gmail.com",
#     department="IT",
#     salary=35000,
#     joining_date=datetime.today()
# )


# employee_instance.post(
#     name="Anu",
#     place="Kochi",
#     mobile="9876543211",
#     email="anu@gmail.com",
#     department="HR",
#     salary=30000,
#     joining_date=datetime.today()
# )



# employee_instance.get()

# employee_instance.retrieve(id=3)


employee_instance.put(
    id=6,
    name="Anu",
    place="Kochi",
    mobile="9876543211",
    email="anu@gmail.com",
    department="HR",
    salary=30000,
    joining_date=datetime.today()
)


# employee_instance.delete(id=3)