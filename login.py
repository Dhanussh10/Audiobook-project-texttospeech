from tkinter import *
from tkinter import messagebox
import pymysql
from tkinter import ttk



def reset():
    if mailentry.get()=='':
        messagebox.showerror('Error','please enter the email address to reset the password')
    else:
        con=pymysql.connect(host='localhost',user='root',password='1234',database='audiobookregistration')
        cur=con.cursor()
        cur.execute('select * from student where email=%s',mailentry.get())
        row=cur.fetchone()
        if row==None:
            messagebox.showerror("Error","please enter the valid email address")
        else:
            con.close()
            def change_password():
                if securityquestionCombo.get()=='Select' or answerEntry.get()=='' or newPassEntry.get()=='':
                    messagebox.showerror('Error','All feilds are required')
                else:
                    con=pymysql.connect(host='localhost',user='root',password='1234',database='audiobookregistration')
                    cur=con.cursor()
                    cur.execute('select * from student where email=%s and question=%s and answer=%s',(mailentry.get(),securityquestionCombo.get(),answerEntry.get()))
                    row=cur.fetchone()
                    if row==None:
                        messagebox.showerror('Error','Security question or answer is incorrect',parent=root2)
                    else:
                        cur.execute('update student set password=%s where email=%s',(newPassEntry.get(),mailentry.get()))
                        con.commit()
                        con.close()
                        messagebox.showinfo('Success','Password is reset, please login with a new password')



            root2=Toplevel()
            root2.title('Forgot password')
            root2.geometry('470x500+400+20')
            root2.config(bg='white')
            image_ = PhotoImage(file='E:\DC slides\hd photos/future.png')
            root2.iconphoto(False, image_)
            root2.focus_force()
            root2.grab_set()
            forgetLabel=Label(root2,text='Forget',font=('times new roman',22,'bold'),bg='white')
            forgetLabel.place(x=100,y=20)
            forgetpasswordLabel = Label(root2, text='Password', font=('times new roman', 22, 'bold'), bg='white',fg='green')
            forgetpasswordLabel.place(x=200, y=20)
            securityqueslabel=Label(root2,text='Security Question',font=('times new roman',19,'bold'),bg='white')
            securityqueslabel.place(x=110, y=90)

            securityquestionCombo=ttk.Combobox(root2,font=('times new roman',19,),state='readonly')
            securityquestionCombo['values']=('Select','Your First Pet Name?','Your Birth Place?','Your best-Friend Name?','Your favorite hobby?')
            securityquestionCombo.place(x=110,y=130)
            securityquestionCombo.current(0)

            answerlabel=Label(root2,text='Answer',font=('times new roman',19,'bold'),bg='white')
            answerlabel.place(x=110,y=180)
            answerEntry=Entry(root2,font=('times new roman',19),bg='white',width=22)
            answerEntry.place(x=110,y=220)

            newPasslabel = Label(root2, text='New Password', font=('times new roman', 19, 'bold'), bg='white')
            newPasslabel.place(x=110, y=270)
            newPassEntry = Entry(root2, font=('times new roman', 19), bg='white',width=22)
            newPassEntry.place(x=110, y=310)

            changepassButton=Button(root2,text='change Password',font=('arial',17,'bold'),bg='green',fg='white',cursor='hand2',activebackground='green',activeforeground='white',command=change_password)
            changepassButton.place(x=110, y=400)





            root2.mainloop

def register_window():
    window.destroy()
    import register

def signin():
    if mailentry.get()=='' or passwordentry.get()=='':
        messagebox.showerror('error','All feilds are required')

    else:
        con=pymysql.connect(host='localhost',user='root',password='1234',database='audiobookregistration')
        cur=con.cursor()
        cur.execute('select * from student where email=%s and password=%s',(mailentry.get(),passwordentry.get()))
        row=cur.fetchone()

        if row==None:
            messagebox.showerror('error','Invalid email or password')
        else:
            messagebox.showinfo('Success','Welcome User')
            window.destroy()
            import main
        con.close()



window=Tk()

image_icon=PhotoImage(file='E:\DC slides\hd photos/future.png')
window.iconphoto(False,image_icon)

window.geometry('900x500+50+50')
window.title('LoginPage')



bgloginimage=PhotoImage(file='loginbg.png')
bgloginLabel=Label(window,image=bgloginimage)
bgloginLabel.place(x=0,y=0)


frame=Frame(window,width=560, height=330,bg='white')
frame.place(x=150,y=75)



maillabel=Label(frame,text='Email',font=('arial',22,'bold'),bg='white')
maillabel.place(x=220,y=32)
mailentry=Entry(frame,font=('arial',22),bg='white')
mailentry.place(x=220,y=75)

passwordlabel=Label(frame,text='password',font=('arial',22,'bold'),bg='white')
passwordlabel.place(x=220, y=120)
passwordentry=Entry(frame,font=('arial',22),bg='white',show="*")
passwordentry.place(x=220,y=163)

regButton=Button(frame,text='Register New Account?',font=('arial',10),bd=0,bg='white',cursor='hand2',activebackground='white',command=register_window)
regButton.place(x=220, y=208)
forgotButton=Button(frame,text='Forgot Password?',font=('arial',10),bd=0,bg='white',fg='red',cursor='hand2',command=reset)
forgotButton.place(x=430,y=208)
LoginButton=Button(frame,text='Login',font=('arial',15),bg='gray20',fg='white',cursor='hand2',command=signin)
LoginButton.place(x=220,y=251)


window.mainloop()