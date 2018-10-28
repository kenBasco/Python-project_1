
import mysql.connector
import random
"""
mydb = mysql.connector.connect(

    host="cs336-group93.cve0ebs2hagy.us-east-2.rds.amazonaws.com",
    user="f18_cs336_93",
    passwd="ninetythree",
    database="BarbeerdrinkerPLUS93"

)


mycursor = mydb.cursor()



    
    for eachL in my_file.readlines():
        
        arrL = eachL.split(",")

        name = arrL[0]
        state = arrL[1]
        tuplekun = (name,state)
        print("namu: " + name + " statu: " + state)

        mysqlFormula = "INSERT INTO drinkers (name, state) VALUES (%s,%s)"

        mycursor.execute(mysqlFormula)

        mydb.commit



sql = "INSERT INTO sample (name, manf) VALUES (%s, %s)"
tuplekun = ("etsg", "nj")
mycursor.execute(sql, tuplekun)

mydb.commit
"""

"""
        arrL = eachL.split(". ")
        


        name = arrL[0]
        state = arrL[1]
        tuplekun = (name,state)
        
        print("INSERT INTO drinkers (name, state) VALUES (" + '"' + name + '"'+ "," + '"' + state + '"' + ");"  )
        """

load = []
load1 = []

with open("states.txt", "r") as my_file:

   

    for eachL in my_file.readlines():
           
        arrL = eachL.split("\n")
     
        load.append(arrL[0])

print(load)

"""
pussy
"""

with open("bars.txt", "r") as my_file:     
        
    

    for eachL in my_file.readlines():
        
        arrL = eachL.split("\n")
        load1.append(arrL[0])
        

for i in range(len(load1)):

    print(load1[i] + "," + random.SystemRandom().choice(load) )


print("done")



