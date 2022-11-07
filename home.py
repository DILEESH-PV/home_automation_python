import mysql.connector
from datetime import datetime
import sys
try:
    mydb=mysql.connector.connect(host='localhost',user='root',password='',database='homeautomationdb')
except mysql.connector.Error as e:
    sys.exit("db connection error")
mycursor=mydb.cursor()
    

while True:
    print("\nSelect an option")
    print("1. Add  a data")
    print("2. View all data")
    print("3. Search data by date")
    print("4. Exit")

    ch = int(input("Enter an option: "))
    
    if (ch==1):
        temp=input("Enter the temperature")
        hum=input("Enter the humidity")
        moi=input("Enter the moisture")
        date=datetime.today().strftime('%Y-%m-%d')
        try:
            sql="INSERT INTO `sensorvalues`(`temperature`, `humidity`, `moisture`, `date`)  VALUES (%s,%s,%s,now())"
            data=(temp,hum,moi)
            mycursor.execute(sql,data)
            mydb.commit()        
            print("inserted success")
        except mysql.connector.Error as e:
            sys.exit("db connection error")
    elif(ch ==2):
        try:
            sql="SELECT `temperature`, `humidity`, `moisture`,`date` FROM `sensorvalues`"
            mycursor.execute(sql)
            result=mycursor.fetchall()
        except mysql.connector.Error as e:
            sys.exit("db connection error")
        for i in result:
            print(i)
        print("Displayed all data")
        
    elif(ch == 3):
        date = input("Enter the date: ")
        sql = "SELECT `temperature`, `humidity`, `moisture` FROM `sensorvalues` WHERE `date`= '"+date+"'"
        mycursor.execute(sql)
        result = mycursor.fetchall()
        print(result)
        mycursor.execute(sql)
        result=mycursor.fetchall()
        for i in result:
            print(i)
        print("Displayed all data")
    elif(ch==4):
        break