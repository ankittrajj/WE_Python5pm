import mysql.connector as c
con = c.connect(host= 'localhost',
                user = 'root',
                passwd = 'Ankit@8285',
                database = 'ybank')

cursor = con.cursor()

# if con.is_connected():
#      print("connected")

# create the menu

while True:

    print("Welcome to Y bank India!!")

    choice = input("1.Open Account\n2.Cash deposit\n3.Cash withdrawl\n4.Account details\n5.Exit")
    # open a/c
    # name
    # mobile num
    # age
    # amount

    if choice == '1':
        name = input("entr the name")
        number = int(input("Enter the mobile number"))
        age = int(input("Enter your age"))
        amount = float (input("Enter the amount"))

        query = "Insert into user values('{}',{},{},{})".format(name,number,age,amount)

        cursor.execute(query)
        con.commit()
        print("Account open successfully!!")


        # choice 2==> cash deposit
        # amount & name

    elif choice == '2':
        amount = float(input('Enter the amount'))
        name = input("Enter the name")

        query = "Update user set amount = {} where name = '{}' ".format(amount,name)
        cursor.execute(query)
        con.commit()
        print('Cash Deposited!!')



        # option number 3
        # cash withdrawl

    elif choice == '3':
        amount = float(input("enter the amount"))
        name = input("enter the name")

        query = "update user set amount = {},where name ='{}'".format(amount,name)
        cursor.execute(query)
        con.commit()
        print("Cash withdrawl")



    # a/c details

    elif choice == '4':
        query = 'select * from user'
        cursor.execute(query)

        acc_details = cursor.fetchmany()
        print(acc_details)
        con.commit()


# exit the code
    elif choice == '5':
        break
