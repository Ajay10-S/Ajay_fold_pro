from tabulate import tabulate
import mysql.connector
con=mysql.connector.connect(host="localhost",user="root",password="Ajay@123",database="python_db")
def insert(name,age,city):
    res=con.cursor()
    qry="insert into users (name,age,city) values(%s,%s,%s)"
    user=(name,age,city)
    res.execute(qry,user)
    con.commit()
    print("Data inserted")
def update(name,age,city,id):
    res=con.cursor()
    qry="update users set name=%s,age=%s,city=%s where id=%s"
    user=(name,age,city,id)
    res.execute(qry,user)
    con.commit()
    print("Data updated")
def delete(id):
    res=con.cursor()
    qry="delete from users where id=%s"
    user=(id,)
    res.execute(qry,user)
    con.commit()
    print("Data deleted")

def select():
    res=con.cursor()
    qry="select * from users"
    res.execute(qry)
    result=res.fetchall()
    print(tabulate(result,headers=["ID","Name","Age","City"]))

while True:
    print("1.insert data")
    print("2.update data")
    print("3.delete data")
    print("4.select data")
    print("5.exit")
    ch=int(input("Enter your choice:"))
    if ch==1:
        name=input("Enter name:")
        age=int(input("Enter Age:"))
        city=input("Enter City:")
        insert(name,age,city)
    elif ch==2:
        id=int(input("enter id:"))
        name = input("Enter name:")
        age = int(input("Enter Age:"))
        city = input("Enter City:")
        update(name,age,city,id)
    elif ch==3:
        id=int(input("enter id:"))
        delete(id)
    elif ch==4:
        select()
    elif ch==5:
        quit()
    else:
        print("Enter invalid")
