import mysql.connector
from datetime import datetime
import sys
try:
    mydb=mysql.connector.connect(host='localhost',user='root',password='',database='homeautomationdb')
except mysql.connector.Error as e:
    sys.exit("db connection error")

while True:
    print("\nSelect an option")
    print("1. Add  a data")
    print("2. View all data")
    print("3. Search data by date")
    print("4. Exit")

    choice = int(input("Enter an option: "))
    if(choice == 1):
        print("Enter the values\n")
    elif(choice ==2):
        print("View all values\n")
    elif(choice == 3):
        print("Search a value\n")
    elif(choice==4):
        break