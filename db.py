import mysql.connector
con=mysql.connector.connect(host="localhost",user="root",password="12345",database="python_db")

class Database():

# if con:
#     print("connected")

   def insert(self,name,age,doj,email,gender,contact,address):
    cur=con.cursor()
    sql="insert into emp(name,age,doj,email,gender,contact,address)values(%s,%s,%s,%s,%s,%s,%s);"
    user=(name,age,doj,email,gender,contact,address)
    cur.execute(sql,user)
    con.commit()
    print("data inserted")

   def update(self,name,age,doj,email,gender,contact,address,id):
    cur=con.cursor()
    sql="update emp set name=%s,age=%s,doj=%s,email=%s,gender=%s,contact=%s,address=%s where id=%s;"
    user=(name,age,doj,email,gender,contact,address,id)
    cur.execute(sql,user)
    con.commit()
    print("updated")
   def delete(self,id):
    cur=con.cursor()
    sql="delete from emp where id=%s;"
    user=(id,)
    cur.execute(sql,user)
    con.commit()
    print("deleted")
   def select(self):
    cur=con.cursor()
    sql="select * from emp"
    cur.execute(sql)
    rows=cur.fetchall()
    return rows
# o=Database()
# o.select()




