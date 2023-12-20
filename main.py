from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from db import Database

db = Database()

root = Tk()
root.title("Employee Management System")
root.geometry("1366x768+0+0")
root.config(bg="#2c3e50")
root.state("zoomed")

name = StringVar()
age = IntVar()
doj=StringVar()
gender=StringVar()
email=StringVar()
contact=IntVar()
address=StringVar()
#entries frame
entries_frame=Frame(root,bg="#535c68",)
entries_frame.pack(side=TOP,fill=X)
title=Label(entries_frame,text="Employee Management System",font=("calibri",18,"bold"),bg="#535c68",fg="white")
#grid means work rows and col
title.grid(row=0,columnspan=2,padx=10,pady=20)
#name
labelName=Label(entries_frame,text="Name",font=("claibri",16),bg="#535c68",fg="white")
labelName.grid(row=1,column=0,padx=10,pady=10)
textName=Entry(entries_frame,textvariable=name,font=("calibri",16),width=30)
textName.grid(row=1,column=1,padx=10,pady=10,sticky="w")
#age
labelAge=Label(entries_frame,text="Age",font=("claibri",16),bg="#535c68",fg="white")
labelAge.grid(row=1,column=2,padx=10,pady=10)
textAge=Entry(entries_frame,textvariable=age,font=("calibri",16),width=30)
textAge.grid(row=1,column=3,padx=10,pady=10,sticky="w")
#doj
labelDoj=Label(entries_frame,text="D.O.J",font=("claibri",16),bg="#535c68",fg="white")
labelDoj.grid(row=2,column=0,padx=10,pady=10)
textDoj=Entry(entries_frame,textvariable=doj,font=("calibri",16),width=30)
textDoj.grid(row=2,column=1,padx=10,pady=10,sticky="w")
#email
labelEmail=Label(entries_frame,text="Email",font=("claibri",16),bg="#535c68",fg="white")
labelEmail.grid(row=2,column=2,padx=10,pady=10)
textEmail=Entry(entries_frame,textvariable=email,font=("calibri",16),width=30)
textEmail.grid(row=2,column=3,padx=10,pady=10,sticky="w")
#gender
labelgen=Label(entries_frame,text="Gender",font=("claibri",16),bg="#535c68",fg="white")
labelgen.grid(row=3,column=0,padx=10,pady=10)
#combo box import
combogen=ttk.Combobox(entries_frame,font=("calibri",16),width=28,textvariable=gender,state="readonly")
combogen['values']=("Male","Female")
combogen.grid(row=3,column=1,padx=10,pady=10,sticky="w")
#contact
labelcontact=Label(entries_frame,text="Contact",font=("claibri",16),bg="#535c68",fg="white")
labelcontact.grid(row=3,column=2,padx=10,pady=10)
textcon=Entry(entries_frame,textvariable=contact,font=("calibri",16),width=30)
textcon.grid(row=3,column=3,padx=10,pady=10,sticky="w")

#address
labeladdr=Label(entries_frame,text="Address",font=("claibri",16),bg="#535c68",fg="white")
labeladdr.grid(row=4,column=0,padx=10,pady=10,sticky="w")
textaddr=Text(entries_frame,width=85,height=5,font=("calibri",16),)
textaddr.grid(row=5,column=0,columnspan=4,sticky="w")

#for btn
def getData(event):
    selected_row=tv.focus()
    data=tv.item(selected_row)
    global row
    row=data["values"]
    #print(row)
    name.set(row[1])
    age.set(row[2])
    doj.set(row[3])
    gender.set(row[5])
    email.set(row[4])
    contact.set(row[6])
    textaddr.delete(1.0,END)
    textaddr.insert(END,row[7])
def displayAll():
    tv.delete(*tv.get_children())
    for row in db.select():
        tv.insert("",END,values=row)
def add_emp():
    if textName.get()=="" or textAge.get()=="" or textDoj.get()=="" or textEmail.get()=="" or textcon.get()=="" or combogen.get()=="" or textaddr.get(
        1.0,END)=="":
        messagebox.showerror("Error in Input","Please Fill All the Detail")
        return
    db.insert(textName.get(),textAge.get(),textDoj.get(),textEmail.get(),combogen.get(),textcon.get(),textaddr.get(
        1.0,END))
    messagebox.showinfo("Success","Record inserted")
    clear_emp()
    displayAll()

def update_emp():
    if textName.get() == "" or textAge.get() == "" or textDoj.get() == "" or textEmail.get() == "" or textcon.get() == "" or combogen.get() == "" or textaddr.get(
            1.0, END) == "":
        messagebox.showerror("Error in Input", "Please Fill All the Detail")
        return
    db.update(textName.get(), textAge.get(), textDoj.get(), textEmail.get(), combogen.get(), textcon.get(),
              textaddr.get(
                  1.0, END),row[0])
    messagebox.showinfo("Success", "Record updated")
    clear_emp()
    displayAll()
def delete_emp():
    db.delete(row[0])
    clear_emp()
    messagebox.showinfo("Success", "Record deleted")
    displayAll()
def clear_emp():
    name.set("")
    age.set("")
    doj.set("")
    gender.set("")
    email.set("")
    contact.set("")
    textaddr.delete(1.0,END)


btn_frame=Frame(entries_frame,bg="#535c68")
btn_frame.grid(row=6,column=0,columnspan=4,padx=10,pady=10,sticky="w")
btnAdd=Button(btn_frame,command=add_emp,text="Add Details",width=15,font=("claibri",16,"bold"),fg="white",
bg="green",bd=0).grid(row=0,column=0,pady=10)

btnUpdate=Button(btn_frame,command=update_emp,text="Update Details",width=15,font=("claibri",16,"bold"),fg="white",
bg="orange",bd=0).grid(row=0,column=1,padx=10,pady=10)

btnDelete=Button(btn_frame,command=delete_emp,text="Delete Details",width=15,font=("claibri",16,"bold"),fg="white",
bg="red",bd=0).grid(row=0,column=2,padx=10,pady=10)

btnClear=Button(btn_frame,command=clear_emp,text="Clear Details",width=15,font=("claibri",16,"bold"),fg="white",
bg="blue",bd=0).grid(row=0,column=3,padx=10,pady=10)

#table frame
tree_frame=Frame(root,bg="#ecf0f1")
tree_frame.place(x=0,y=480,width=1366,height=700)
style=ttk.Style()
style.configure("mystyle.Treeview",font=('colibri',18),rowheight=50)#modify font body


style.configure("mystyle.Treeview.Heading",font=('colibri',18))
tv=ttk.Treeview(tree_frame,columns=(1,2,3,4,5,6,7,8),style="mystyle.Treeview")
tv.heading("1",text="ID")
tv.column("1",width=5)
tv.heading("2",text="Name")
tv.column("2",width=60)

tv.heading("3",text="Age")
tv.column("3",width=5)
tv.heading("4",text="D.O.J")
tv.column("4",width=10)
tv.heading("5",text="Email")
tv.column("5",width=60)
tv.heading("6",text="Gender")
tv.column("6",width=25)
tv.heading("7",text="Contact")
tv.column("7",width=30)
tv.heading("8",text="Address")
tv['show']='headings'
tv.bind("<ButtonRelease-1>",getData)
tv.pack(fill=X)
#for continue run  until close button x

displayAll()
clear_emp()#int type default placeholder-> 0
root.mainloop()
