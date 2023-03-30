import pypyodbc

mySQLServer = "SERVERNAME\SQLEXPRESS"
myDatabase = "BASENAME"

connection = pypyodbc.connect('Driver={SQL Server};'
                              'Server=' + mySQLServer + ';'
                              'Database=' + myDatabase + ';'
                              'uid=username;'
                              'pwd=password;')

cursor = connection.cursor()

mySQLQuery = ("""
                SELECT CompanyName, ContactName, country
                FROM dbo.Customers
                WHERE country = 'Canada'
               """)

cursor.execute(mySQLQuery)
results = cursor.fetchall()

for row in results:
    companyname = row[0]
    contactname = row[1]
    contryname = row[2]

    print("Welcome :" + str(companyname) + " User: " + str(contactname) + " From: " + str(contryname))

connection.close()