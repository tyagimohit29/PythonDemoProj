import pyodbc

def read(conn):
    print("read")
    cursor = conn.cursor()
    cursor.execute("select * from projects where project_num=3335")

    for row in cursor:
        print(row)


conn = pyodbc.connect(
    "Driver={SQL Server Native Client 11.0};"
    "Server=10.14.109.71,62079;"
    "Database=dev_major_cop_001;"
    "Trusted_Connection=yes;"
)

read(conn)
conn.close()