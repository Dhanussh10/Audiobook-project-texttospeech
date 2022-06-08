from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *
import pymysql
from tkinter.ttk import Combobox
from tkinter import messagebox

def clear():
    entryfirstname.delete(0,END)
    entrylastname.delete(0,END)
    entrycontact.delete(0,END)
    entryEmail.delete(0,END)
    entryAnswer.delete(0,END)
    entrypassword.delete(0,END)
    confirmpasswordentry.delete(0,END)
    comboquestion.current(0)

def page():
    root.destroy()
    import login

def register():
    if entryfirstname.get()=='' or entrylastname.get()=='' or entryEmail.get()=='' or entrycontact.get()==''\
        or entrypassword.get()=='' or confirmpasswordentry.get()=='' or comboquestion.get()=='Select' or entryAnswer.get()=='':
        messagebox.showerror('Error','All feilds are required')

    elif entrypassword.get() != confirmpasswordentry.get():
        messagebox.showerror("Error","password mismatch please check")

    else:
        con=pymysql.connect(host='localhost',user='root',password='1234',database='audiobookregistration')
        cur=con.cursor()
        cur.execute('select * from student where email=%s',entryEmail.get())
        row=cur.fetchone()
        if row!=None:
            messagebox.showerror('Error','User already exists')
        else:
            cur.execute('insert into student(f_name,l_name,contact,email,question,answer,password) values(%s,%s,%s,%s,%s,%s,%s)',(entryfirstname.get(),entrylastname.get(),entrycontact.get(),entryEmail.get(),comboquestion.get(),entryAnswer.get(),entrypassword.get()))
            con.commit()
            con.close()
            messagebox.showinfo('success','Registration is successfull')
            clear()
            root.destroy()
            import login




root=Tk()

root.geometry('1350x690+10+10')
root.title('Registration Form')
root.configure(bg='darkblue')

bgimage=PhotoImage(file="bg.png")
bgLabel=Label(root,image=bgimage)
bgLabel.place(x=10,y=85)

image_icon=PhotoImage(file="E:\DC slides\hd photos/future.png")
root.iconphoto(False,image_icon)

registerFrame=Frame(root, width=460, height=500)
registerFrame.place(x=580, y=30)

titleLabel=Label(registerFrame,text="Regisration Form",font=('arial',22,'bold'),fg='gold')
titleLabel.place(x=20,y=5)

firstnameLabel=Label(registerFrame,text='First Name',font=('times new roman',15,'bold'),fg="gray20")
firstnameLabel.place(x=20,y=60)
entryfirstname=Entry(registerFrame,font=('times new roman',11),bg="lightgray")
entryfirstname.place(x=20,y=100)

lastnameLabel=Label(registerFrame,text='Last Name',font=('times new roman',15,'bold'),fg='gray20')
lastnameLabel.place(x=270,y=60)
entrylastname=Entry(registerFrame,font=('times new roman',11),bg='lightgray')
entrylastname.place(x=270,y=100)

contactLabel=Label(registerFrame,text='Contact.No',font=('times new roman',15,'bold'),fg='gray20')
contactLabel.place(x=20,y=150)
entrycontact=Entry(registerFrame,font=('times new roman',11),bg='lightgray')
entrycontact.place(x=20,y=190)

emailLabel=Label(registerFrame,text='Email',font=('times new roman',15,'bold'),fg='gray20')
emailLabel.place(x=270,y=150)
entryEmail=Entry(registerFrame,font=('times new roman',11),bg='lightgray')
entryEmail.place(x=270,y=190)

QuestionLabel=Label(registerFrame,text='Security Question',font=('times new roman',15,'bold'),fg='gray20')
QuestionLabel.place(x=20,y=240)
comboquestion=Combobox(registerFrame,font=('times new roman',11),state="readonly")
comboquestion['values']=('Select','Your first pet name?','Your birth place?','Your best-friend name?','Your favorite hobby?')
comboquestion.set('select')
comboquestion.place(x=20,y=280)

answerLabel=Label(registerFrame,text='Answer',font=('times new roman',15,'bold'),fg='gray20')
answerLabel.place(x=270,y=240)
entryAnswer=Entry(registerFrame,font=('times new roman',11),bg='lightgray')
entryAnswer.place(x=270, y=280)

passwordLabel=Label(registerFrame,text='Password',font=('times new roman',15,'bold'),fg='gray20')
passwordLabel.place(x=20,y=330)
entrypassword=Entry(registerFrame,font=('times new roman',11),bg='lightgray',show='*')
entrypassword.place(x=20, y=370)

confirmpasswordLabel=Label(registerFrame,text='Confirm Password',font=('times new roman',15,'bold'),fg='gray20')
confirmpasswordLabel.place(x=270,y=330)
confirmpasswordentry=Entry(registerFrame,font=('times new roman',11),bg='lightgray',show="*")
confirmpasswordentry.place(x=270, y=370)

buttonimage=PhotoImage(file="button.png")
registerButton=Button(registerFrame,image=buttonimage,bd=0,cursor="hand2",command=register)
registerButton.place(x=150,y=420)

loginimage=PhotoImage(file="login.png")
loginButton=Button(root,image=loginimage,bd=0,bg="gold",cursor="hand2",command=page)
loginButton.place(x=75,y=245)





root.mainloop()