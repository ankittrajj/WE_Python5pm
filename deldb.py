import mysql.connector as c
con = c.connect(host = 'localhost',
                user = 'root',
                passwd = 'Ankit@8285',
                database = 'python')

cursor = con.cursor()
# if con.is_connected():
#     print("connected!!")


#name,age & marks --> user input!!
# name = input("Enter the name")
age = int(input("enter the age"))
# marks = float (input("Enter your marks"))

query = "delete from user where age ={}".format(age)
cursor.execute(query)
con.commit()
print("data deleted successfully!!")
