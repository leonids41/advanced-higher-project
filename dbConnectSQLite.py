import sqlite3
connection = sqlite3.connect("exampleTwo.db")
cursor = connection.cursor()

createQuerry = "CREATE TABLE IF NOT EXISTS testing (id integer NOT NULL, name varchar (10) NOT NULL, PRIMARY KEY (id));"
    


cursor.execute(createQuerry)

cursor.execute("INSERT INTO testing VALUES (17, 'Mr Hendry')")
connection.commit


cursor.execute("SELECT * FROM testing")
result = cursor.fetchall()

temp2Dlist = []
colNames = [description[0] for description in cursor.description]
temp2Dlist.append(colNames)

for each in result: 
    temprow = []
    for loop in range (0, len(each)):
        temprow.append(each[loop])
    temp2Dlist.append(temprow)


print (temp2Dlist[0][1] +"  " + temp2Dlist[0][0])
print (temp2Dlist[1][1] +"  " + str(temp2Dlist[1][0]))



