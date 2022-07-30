import mysql.connector as c
con = c.connect(host = 'localhost',
                user = 'root',
                passwd = 'Ankit@8285',
                database = 'project')

cursor = con.cursor()

# if con.is_connected():
#     print("connection successfully!!")


choice = input("1.Open A/c\n2.Cash Withdrawl\n3.Cash deposit\n4.Account Details\n5.Exit")

if choice == '1':
    name= input("entr the name")
    age = int(input("entr the age"))
    number = int(input("entr the number"))
    query =  "insert into user values('{}',{},{})".format(name,age,number)
    cursor.execute(query)
    con.commit()
    print("Data eneterd successfully!!")

elif choice == '2':
    name = input("Enter the name")
    number = int(input("enter the amount"))

    query = 