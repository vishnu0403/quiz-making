#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tkinter as tk
from tkinter import *
from tkinter import messagebox
import sqlite3
import time
import smtplib
import random
import subprocess
import os



#data='database.db'
root=tk.Tk()
root.geometry('1400x730')
root.title('quiz')

h1=tk.StringVar()
h2=tk.StringVar()
h3=tk.StringVar()
h4=tk.StringVar()
p2=tk.StringVar()
p3=tk.StringVar()
p1=tk.IntVar()
n1=tk.StringVar()
n2=tk.StringVar()
var=tk.IntVar()
varf1=tk.IntVar()
lan=tk.IntVar()
varf2=tk.StringVar()
l2=StringVar()

#global variables

global fi1
global fi2

anu="ab"
c=0
mar=0
har=1
Answer='A'
data='database'
qus=1
List1=['N','N','N','N','N','N','N','N','N','N']
List=['a','b','c','d','e','f','g','h','i','j']
a="abhay"
global b
global d


#it is use to encode the password.............
def encode(s):
    i=0
    a=""
    h="!@#"
    while i<len(s):
        #print (s[i])
        if(s[i]=='a' or s[i]=='A' or s[i]=='e' or s[i]=='E'
           or s[i]=='i' or s[i]=='I' or s[i]=='o' or s[i]=='O'
           or s[i]=='u' or s[i]=='U'):
            b=chr(ord(s[i])-25)
            a=a+b
            i=i+1
        elif(s[i]=='0' or s[i]=='1' or s[i]=='2' or s[i]=='3'
           or s[i]=='4' or s[i]=='5' or s[i]=='6' or s[i]=='7'
           or s[i]=='8' or s[i]=='9'):
            b=chr(ord(s[i])-14)
            a=a+b+h
            i=i+1
        else:
            b=chr(ord(s[i])+4)
            a=a+b
            i=i+1
    return (a)
        
    
# it is use for to check the password is right or not, when the user enter the enrollment numnber then check it it is right or not
def enroll(f1):
    global data
    global anu
    tn1=n1.get()
    tn3=n2.get()
    z=encode(tn3)
    if(tn1==''):
        m="Plzz!!! enter your Enrollment Number"
        messagebox.showerror("Error!", m)
    else:
        global c    
        ac=False
        conn=sqlite3.connect(data)
        #cursor=conn.cursor()
        temp=conn.execute('SELECT Name,Password,Enroll,Email FROM DATA WHERE Enroll=?',(tn1,))
        for i in temp:
            ac=i[2]
            anu=i[3]
            
            if (i[2]==tn1):
                ac = True
                con=conn.execute('SELECT marks FROM ANS WHERE enroll=?',(tn1,))
                ttt=con.fetchone()
                san=ttt[0]
                print (san)
                if(san!='N'):    
                    m="You are already play quiz with this Enrollment Number"
                    messagebox.showerror("Error!", m)
                else:
                    if (i[1]==z):
                        ac = True
                        m = "{} Login SucessFull".format(i[0])
                        messagebox.showinfo("Login Info", m)
                        f1.destroy()
                        Main()
                    else:
                        c=c+1
                        ac = True
                        m = " Login UnSucessFull ! Wrong Password"
                        messagebox.showerror("Login Info!", m)
                        if(c==3):
                            m="Sorry you reach Max Time Limit for login"
                            messagebox.showerror("Login Info", m)
                            root.destroy()
                        
        if not ac:
            m = "SORRY YOU ARE ENTER WORNG ENROLLMENT NUMBER!"
            messagebox.showwarning("Login Info!", m)

#it is the back bone of the hole code. because question are come from database, answer are storage in database also   
def Main():

    def sub():
        global List
        global List1
        global mar
        global data
        global anu
        mar=0
        a1=n1.get()
        print (a1)
        t=tuple(List1)    
        t1=tuple(List)
        k=0
        for i in t:
            if(i==t1[k]):
                mar=mar+1
            else:
                mar=mar
            k=k+1
        print (mar)
        conn=sqlite3.connect(data)
        with conn:
            cursor=conn.cursor()
        cursor.execute('UPDATE ANS SET marks=? WHERE enroll=?',(mar,a1))
        conn.commit()
        root.destroy()
    
    def countdown(t=600):
        print ("yes")
        mins, secs = divmod(t, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        l.config(text=str(timeformat))
        print(timeformat,)
        root.after(1000,countdown,t-1)
        if(mins==00 and secs==00):
            print('Goodbye!\n\n\n\n\n')
            sub()
    
    #it is use to count the marks of right answer and then storage the marksin the database.........
    def Quit():
        global List
        global List1
        global mar
        global data
        global anu
        mar=0
        a1=n1.get()
        print (a1)
        t=tuple(List1)    
        t1=tuple(List)
        k=0
        for i in t:
            if(i==t1[k]):
                mar=mar+1
            else:
                mar=mar
            k=k+1
        print (mar)
        conn=sqlite3.connect(data)
        with conn:
            cursor=conn.cursor()
        cursor.execute('UPDATE ANS SET marks=? WHERE enroll=?',(mar,a1))
        conn.commit()
        m = "Do you want to get your marks on mail"
        xyz=messagebox.askyesno("Submit Info!", m)
        if(xyz==True):
            print (anu)
            email_send=anu
            email_user='sahua545@gmail.com'
            m = "Wait for a minter while mail is sending"
            messagebox.showinfo("Email information!", m)
            server=smtplib.SMTP('smtp.gmail.com',587)
            server.starttls()
            server.login(email_user,'123harshita321')
            message="You got "+str(mar)+" in the quiz you can do more better!! but Thanks to use the form"
            server.sendmail(email_user,email_send,message)
            server.quit()
            root.destroy()
        else:
            m = "Do you want to see your marks write now!!"
            wxyz=messagebox.askyesno("Submit Info!", m)
            if(wxyz==True):
                m = "Your marks in Quiz is:- {}!!".format(mar)
                wxyz=messagebox.showinfo("Submit Info!", m)
                root.destroy()
            else:
                m = "Thank You for Using This"
                wxyz=messagebox.showinfo("Submit Info!", m)
                root.destroy()


#it is used when we click
    def Next():
        try:
            global Answer
            global qus
            global data
            global List1
            ab=var.get()
            a1=qus+1
            if(a1>10):
                a1=1
            else:
                a1=a1
            #a1=har
            if(a1==10):
                logbtn1=tk.Button(root, text="Submit", font=("bold",20),bd=5, command=Quit).place(x=500,y=600)
                
            conn=sqlite3.connect(data)
            with conn:
                cursor=conn.cursor()
            cursor.execute('CREATE TABLE IF NOT EXISTS QUS(Qus_no INTEGER,Qusetion TEXT,Option_A TEXT,Option_B TEXT,Option_C TEXT,Option_D TEXT,Answer TEXT)')
            con=cursor.execute('SELECT Qus_no, Qusetion,Option_A,Option_B,Option_C,Option_D,Answer FROM QUS WHERE Qus_no=?',(a1,))
            t=con.fetchone()
            qus=t[0]
            Qusetion=t[1]
            Option_A=t[2]
            Option_B=t[3]
            Option_C=t[4]
            Option_D=t[5]
            Answer=t[6]

            xy=List1[qus-1]
        
        
            rb5=Radiobutton(root,text="",variable=varf1,value=5,bd=5,font=("bold",1))
            rb5.place(x=1500,y=250)
            rb5.select()
        
            f2=Frame(root,width=800,height=400,bg="silver",relief=SUNKEN)
            f2.place(x=50,y=150)

            label2=tk.Label(f2,text=Qusetion,bg="silver",font=("bold",15))
            label2.place(x=10,y=30)
            if(xy=="A"):
                rb1=Radiobutton(f2,text=Option_A,variable=varf1,value=1,bd=5,fg="Green",font=("bold",15))
                rb1.place(x=10,y=100)
                rb1.select()
                rb2=Radiobutton(f2,text=Option_B,variable=varf1,value=2,bd=5,font=("bold",15))
                rb2.place(x=10,y=150)
                rb3=Radiobutton(f2,text=Option_C,variable=varf1,value=3,bd=5,font=("bold",15))
                rb3.place(x=10,y=200)
                rb4=Radiobutton(f2,text=Option_D,variable=varf1,value=4,bd=5,font=("bold",15))
                rb4.place(x=10,y=250)
            elif(xy=="B"):
                rb1=Radiobutton(f2,text=Option_A,variable=varf1,value=1,bd=5,font=("bold",15))
                rb1.place(x=10,y=100)
                rb2=Radiobutton(f2,text=Option_B,variable=varf1,value=2,bd=5,fg="Green",font=("bold",15))
                rb2.place(x=10,y=150)
                rb2.select()
                rb3=Radiobutton(f2,text=Option_C,variable=varf1,value=3,bd=5,font=("bold",15))
                rb3.place(x=10,y=200)
                rb4=Radiobutton(f2,text=Option_D,variable=varf1,value=4,bd=5,font=("bold",15))
                rb4.place(x=10,y=250)
            elif(xy=="C"):
                rb1=Radiobutton(f2,text=Option_A,variable=varf1,value=1,bd=5,font=("bold",15))
                rb1.place(x=10,y=100)
                rb2=Radiobutton(f2,text=Option_B,variable=varf1,value=2,bd=5,font=("bold",15))
                rb2.place(x=10,y=150)
                rb3=Radiobutton(f2,text=Option_C,variable=varf1,value=3,bd=5,fg="Green",font=("bold",15))
                rb3.place(x=10,y=200)
                rb3.select()
                rb4=Radiobutton(f2,text=Option_D,variable=varf1,value=4,bd=5,font=("bold",15))
                rb4.place(x=10,y=250)
            elif(xy=="D"):
                rb1=Radiobutton(f2,text=Option_A,variable=varf1,value=1,bd=5,font=("bold",15))
                rb1.place(x=10,y=100)
                rb2=Radiobutton(f2,text=Option_B,variable=varf1,value=2,bd=5,font=("bold",15))
                rb2.place(x=10,y=150)
                rb3=Radiobutton(f2,text=Option_C,variable=varf1,value=3,bd=5,font=("bold",15))
                rb3.place(x=10,y=200)
                rb4=Radiobutton(f2,text=Option_D,variable=varf1,value=4,bd=5,fg="Green",font=("bold",15))
                rb4.place(x=10,y=250)
                rb4.select()
            else:
                rb1=Radiobutton(f2,text=Option_A,variable=varf1,value=1,bd=5,font=("bold",15))
                rb1.place(x=10,y=100)
                rb2=Radiobutton(f2,text=Option_B,variable=varf1,value=2,bd=5,font=("bold",15))
                rb2.place(x=10,y=150)
                rb3=Radiobutton(f2,text=Option_C,variable=varf1,value=3,bd=5,font=("bold",15))
                rb3.place(x=10,y=200)
                rb4=Radiobutton(f2,text=Option_D,variable=varf1,value=4,bd=5,font=("bold",15))
                rb4.place(x=10,y=250)
                rb5=Radiobutton(root,text="",variable=varf1,value=5,bd=5,font=("bold",1))
                rb5.place(x=1500,y=250)
                rb5.select()  

        except TypeError:  
            m = "it is a last question and answer of this question is submited, know u can quit the quiz"
            messagebox.showinfo("Qustion Infomation", m)
        
    
    def summit():
        global Answer
        global qus
        global data
        A1=Answer
        aa=(varf1.get())     
        b2=qus
        tn1=(n1.get())
        re=tn1
 
        if(aa==1):
            b1="A"
            List1[b2-1]=b1
            List[b2-1]=A1
        elif(aa==2):
            b1="B"
            List1[b2-1]=b1
            List[b2-1]=A1
        elif(aa==3):
            b1="C"
            List1[b2-1]=b1
            List[b2-1]=A1
        else:
            b1="D"
            List1[b2-1]=b1
            List[b2-1]=A1
        if(b1==A1):
            b1="{} Right".format(b1)
        else:
            b1="{} wrong ({}) ".format(b1,A1)
            
        conn=sqlite3.connect(data)
        with conn:
            cursor=conn.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS ANS(enroll Text,Q1 TEXT,Q2 TEXT,Q3 TEXT,Q4 TEXT,Q5 TEXT,Q6 TEXT,Q7 TEXT,Q8 TEXT,Q9 TEXT,Q10 TEXT,marks INTEGER)')
        if(b2==1):
            cursor.execute('UPDATE ANS SET Q1=? WHERE enroll=?',(b1,re))
            conn.commit()
        elif(b2==2):
            cursor.execute('UPDATE ANS SET Q2=? WHERE enroll=?',(b1,re))
            conn.commit()
        elif(b2==3):
            cursor.execute('UPDATE ANS SET Q3=? WHERE enroll=?',(b1,re))
            conn.commit()
        elif(b2==4):
            cursor.execute('UPDATE ANS SET Q4=? WHERE enroll=?',(b1,re))
            conn.commit()
        elif(b2==5):
            cursor.execute('UPDATE ANS SET Q5=? WHERE enroll=?',(b1,re))
            conn.commit()
        elif(b2==6):
            cursor.execute('UPDATE ANS SET Q6=? WHERE enroll=?',(b1,re))
            conn.commit()
        elif(b2==7):
            cursor.execute('UPDATE ANS SET Q7=? WHERE enroll=?',(b1,re))
            conn.commit()
        elif(b2==8):
            cursor.execute('UPDATE ANS SET Q8=? WHERE enroll=?',(b1,re))
            conn.commit()
        elif(b2==9):
            cursor.execute('UPDATE ANS SET Q9=? WHERE enroll=?',(b1,re))
            conn.commit()
        elif(b2==10):
            cursor.execute('UPDATE ANS SET Q10=? WHERE enroll=?',(b1,re))
            conn.commit()
        Next()



    def qus():
        global Answer
        global qus
        global data
        global List1
        a1=(var.get())
        if(qus==10):
            logbtn1=tk.Button(root, text="Submit", font=("bold",20),bd=5, command=Quit).place(x=500,y=600)
        conn=sqlite3.connect(data)
        with conn:
            cursor=conn.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS QUS(Qus_no INTEGER,Qusetion TEXT,Option_A TEXT,Option_B TEXT,Option_C TEXT,Option_D TEXT,Answer TEXT)')
        con=cursor.execute('SELECT Qus_no, Qusetion,Option_A,Option_B,Option_C,Option_D,Answer FROM QUS WHERE Qus_no=?',(a1,))
        t=con.fetchone()
        qus=t[0]
        Qusetion=t[1]
        Option_A=t[2]
        Option_B=t[3]
        Option_C=t[4]
        Option_D=t[5]
        Answer=t[6]

        xy=List1[qus-1]

        if(qus==10):
            logbtn1=tk.Button(root, text="Submit", font=("bold",20),bd=5, command=Quit).place(x=500,y=600)
        
        
        rb5=Radiobutton(root,text="",variable=varf1,value=5,bd=5,font=("bold",1))
        rb5.place(x=1500,y=250)
        rb5.select()
    
        f2=Frame(root,width=900,height=400,bg="silver",relief=SUNKEN)
        f2.place(x=50,y=150)

        label2=tk.Label(f2,text=Qusetion,bg="silver",font=("bold",15))
        label2.place(x=10,y=30)
        if(xy=="A"):
            rb1=Radiobutton(f2,text=Option_A,variable=varf1,value=1,bd=5,fg="Green",font=("bold",15))
            rb1.place(x=10,y=100)
            rb1.select()
            rb2=Radiobutton(f2,text=Option_B,variable=varf1,value=2,bd=5,font=("bold",15))
            rb2.place(x=10,y=150)
            rb3=Radiobutton(f2,text=Option_C,variable=varf1,value=3,bd=5,font=("bold",15))
            rb3.place(x=10,y=200)
            rb4=Radiobutton(f2,text=Option_D,variable=varf1,value=4,bd=5,font=("bold",15))
            rb4.place(x=10,y=250)
        elif(xy=="B"):
            rb1=Radiobutton(f2,text=Option_A,variable=varf1,value=1,bd=5,font=("bold",15))
            rb1.place(x=10,y=100)
            rb2=Radiobutton(f2,text=Option_B,variable=varf1,value=2,bd=5,fg="Green",font=("bold",15))
            rb2.place(x=10,y=150)
            rb2.select()
            rb3=Radiobutton(f2,text=Option_C,variable=varf1,value=3,bd=5,font=("bold",15))
            rb3.place(x=10,y=200)
            rb4=Radiobutton(f2,text=Option_D,variable=varf1,value=4,bd=5,font=("bold",15))
            rb4.place(x=10,y=250)
        elif(xy=="C"):
            rb1=Radiobutton(f2,text=Option_A,variable=varf1,value=1,bd=5,font=("bold",15))
            rb1.place(x=10,y=100)
            rb2=Radiobutton(f2,text=Option_B,variable=varf1,value=2,bd=5,font=("bold",15))
            rb2.place(x=10,y=150)
            rb3=Radiobutton(f2,text=Option_C,variable=varf1,value=3,bd=5,fg="Green",font=("bold",15))
            rb3.place(x=10,y=200)
            rb3.select()
            rb4=Radiobutton(f2,text=Option_D,variable=varf1,value=4,bd=5,font=("bold",15))
            rb4.place(x=10,y=250)
        elif(xy=="D"):
            rb1=Radiobutton(f2,text=Option_A,variable=varf1,value=1,bd=5,font=("bold",15))
            rb1.place(x=10,y=100)
            rb2=Radiobutton(f2,text=Option_B,variable=varf1,value=2,bd=5,font=("bold",15))
            rb2.place(x=10,y=150)
            rb3=Radiobutton(f2,text=Option_C,variable=varf1,value=3,bd=5,font=("bold",15))
            rb3.place(x=10,y=200)
            rb4=Radiobutton(f2,text=Option_D,variable=varf1,value=4,bd=5,fg="Green",font=("bold",15))
            rb4.place(x=10,y=250)
            rb4.select()
        else:
            rb1=Radiobutton(f2,text=Option_A,variable=varf1,value=1,bd=5,font=("bold",15))
            rb1.place(x=10,y=100)
            rb2=Radiobutton(f2,text=Option_B,variable=varf1,value=2,bd=5,font=("bold",15))
            rb2.place(x=10,y=150)
            rb3=Radiobutton(f2,text=Option_C,variable=varf1,value=3,bd=5,font=("bold",15))
            rb3.place(x=10,y=200)
            rb4=Radiobutton(f2,text=Option_D,variable=varf1,value=4,bd=5,font=("bold",15))
            rb4.place(x=10,y=250)
            rb5=Radiobutton(root,text="",variable=varf1,value=5,bd=5,font=("bold",1))
            rb5.place(x=1500,y=250)
            rb5.select()
    
            
        

                        
    logbtn=tk.Button(root, text="Next", command=summit,bd=5, font=("bold",20)).place(x=230,y=600)
    #logbtn1=tk.Button(root, text="Submit", font=("bold",20),bd=5, command=Quit).place(x=500,y=600)        
    #logbtn2=tk.Button(root, text="Next", font=("bold",20), command=Next).place(x=400,y=600)
         

    
    f1=Frame(root,width=320,height=310,bg="silver",relief=SUNKEN)
    f1.place(x=1000,y=230)

    f30=Frame(root,width=900,height=400,bg="silver",relief=SUNKEN)
    f30.place(x=50,y=150)


    rbf1=Radiobutton(f1,text="Q1",variable=var,value=1,bd=5, command=qus,font=("bold",12))
    rbf1.place(x=10,y=10)

    rbf2=Radiobutton(f1,text="Q2",variable=var,value=2,bd=5, command=qus,font=("bold",12))
    rbf2.place(x=90,y=10)

    rbf3=Radiobutton(f1,text="Q3",variable=var,value=3,bd=5, command=qus,font=("bold",12))
    rbf3.place(x=170,y=10)

    rbf4=Radiobutton(f1,text="Q4",variable=var,value=4,bd=5, command=qus,font=("bold",12))
    rbf4.place(x=250,y=10)

    rbf5=Radiobutton(f1,text="Q5",variable=var,value=5,bd=5, command=qus,font=("bold",12))
    rbf5.place(x=10,y=90)

    rbf6=Radiobutton(f1,text="Q6",variable=var,value=6,bd=5, command=qus,font=("bold",12))
    rbf6.place(x=90,y=90)

    rbf7=Radiobutton(f1,text="Q7",variable=var,value=7,bd=5, command=qus,font=("bold",12))
    rbf7.place(x=170,y=90)

    rbf8=Radiobutton(f1,text="Q8",variable=var,value=8,bd=5, command=qus,font=("bold",12))
    rbf8.place(x=250,y=90)

    rbf9=Radiobutton(f1,text="Q9",variable=var,value=9,bd=5, command=qus,font=("bold",12))
    rbf9.place(x=10,y=170)

    rbf10=Radiobutton(f1,text="Q10",variable=var,value=10,bd=5, command=qus,font=("bold",12))
    rbf10.place(x=90,y=170)

    l=Label(root,text="start",width=10,bd=5,bg="red",font=("bold",20))
    l.place(x=1100,y=150)

    countdown()


#it is use to chane the password or when user forget the password then this function is called
def change(y,f6):
    global data
    re=n1.get()
    pp1=p1.get()
    pp2=p2.get()
    pp3=p3.get()
    
    f99=Frame(root,width=1,height=1)
    f99.place(x=1500,y=100)
    if(y==pp1):
        if(pp2==pp3):
            b1=encode(pp2)
            m = "Password Has Update SucessFull"
            messagebox.showinfo("Password information", m)
            conn=sqlite3.connect(data)
            cursor=conn.cursor()
            cursor.execute('UPDATE DATA SET Password=? WHERE enroll=?',(b1,re))
            conn.commit()
            f6.destroy()
            login(f99)
            
            #root.destroy()
        else:
            m = "Both Password Are Not Same"
            messagebox.showerror("Error!!!!", m)
    else:
        m = "Configration Number Is Not Same"
        messagebox.showinfo("Login Info", m)

# it is made the GUI form for forget password or send the mail on the given E-mail.. 
def forget(f5):
    global data
    a1=n1.get()
    y=random.randint(10000,99999)
    f5.destroy
    conn=sqlite3.connect(data)
    cursor=conn.cursor()
    con=cursor.execute('SELECT Email FROM DATA WHERE enroll=?',(a1,))
    try:
        t=con.fetchone()
        # code for send for a mail to to change the password or forget the password
        email_send=t[0]
        email_user='sahua545@gmail.com'
        m = "Wait for a minter while mail is sending"
        messagebox.showinfo("Email information!", m)
        server=smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login(email_user,'123harshita321')
        message=str(y)+" is a verification code for change the password or forget the password"
        server.sendmail(email_user,email_send,message)
        server.quit()
        m = "verification code is send on your email addres, Do u want to change the password"
        harshi=messagebox.askyesno("Email information!", m)
        if(harshi==True):

            f6=Frame(root,width=600,height=400,bg="silver",relief=SUNKEN)
            f6.place(x=300,y=160)

            label=tk.Label(f6,text="FORGET PASSWORD",bd=5,font=("bold",20))
            label.place(x=150,y=30)

            label2=tk.Label(f6,text="Enter pin form your mail:-",bd=5,font=("bold",15))
            label2.place(x=70,y=120)
            entry_1=tk.Entry(f6, textvariable=p1,bd=5,font=("bold",15)).place(x=310,y=120)

            label3=tk.Label(f6,text="Create New Password:- ",bd=5,font=("bold",15))
            label3.place(x=70,y=180)
            entry_2=tk.Entry(f6, textvariable=p2,bd=5,font=("bold",15)).place(x=310,y=180)

            label4=tk.Label(f6,text="Enter Password Again:- ",bd=5,font=("bold",15))
            label4.place(x=70,y=230)
            entry_3=tk.Entry(f6, textvariable=p3,bd=5,font=("bold",15)).place(x=310,y=230)        

            logbtn2=tk.Button(f6,text="change",bd=5,command=lambda: change(y,f6),font=("bold",15)).place(x=250,y=300)

        else:
            root.destroy()
    except TypeError:
        m = "This Enrolment number does to exist"
        messagebox.showinfo("Not Exist!", m)
            
            

def login(f5):
    f5.destroy()
    global fi1
    global fi2
    fi1.destroy()
    fi2.destroy()
    global a

    f11=Frame(root,width=600,height=400,bg="silver",relief=SUNKEN)
    f11.place(x=300,y=160)

    ll=Label(f11,image=a,width=80,height=80,bd=5,relief=SUNKEN)
    ll.place(x=50,y=25)

    label=tk.Label(f11,text="WELCOME FOR QUIZ",bd=5,font=("bold",20))
    label.place(x=150,y=30)

    label2=tk.Label(f11,text="Enter your Enrollment:- ",bd=5,font=("bold",15))
    label2.place(x=70,y=120)

    entry_1=tk.Entry(f11, textvariable=n1,bd=5,font=("bold",15)).place(x=290,y=120)

    label2=tk.Label(f11,text="Enter your Password:- ",bd=5,font=("bold",15))
    label2.place(x=70,y=180)

    entry_1=tk.Entry(f11, textvariable=n2,bd=5,show="*",font=("bold",15)).place(x=290,y=180)
    logbtn2=tk.Button(f11,text="Submit",bd=5,command=lambda:enroll(f11),font=("bold",15)).place(x=250,y=250)
    logbtn3=tk.Button(f11,text="Forget Password",bd=5,command=lambda:forget(f11),font=("bold",15)).place(x=230,y=320)

def okk(f3,f5,e2):
    try:
        global data
        ah1=h1.get()
        ah2=h2.get()
        ah3=h3.get()
        ah4=h4.get()
        tn2="N"
        y=encode(ah4)
        conn=sqlite3.connect(data)
        with conn:
            cursor=conn.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS DATA(Enroll Text,Password TEXT,Name TEXT,Email TEXT)')
        cursor.execute('INSERT INTO DATA(Enroll,Password,Name,Email)VALUES(?,?,?,?)',(ah3,y,ah1,ah2))
        
        cursor.execute('CREATE TABLE IF NOT EXISTS ANS(enroll Text,Q1 TEXT,Q2 TEXT,Q3 TEXT,Q4 TEXT,Q5 TEXT,Q6 TEXT,Q7 TEXT,Q8 TEXT,Q9 TEXT,Q10 TEXT,marks INTEGER)')
        cursor.execute('INSERT INTO ANS(enroll,Q1,Q2,Q3,Q4,Q5,Q6,Q7,Q8,Q9,Q10,marks) VALUES(?,?,?,?,?,?,?,?,?,?,?,?)',(ah3,tn2,tn2,tn2,tn2,tn2,tn2,tn2,tn2,tn2,tn2,tn2)) 
        conn.commit()
        m ="{} are you Register Successfully!!".format(ah1)
        messagebox._show("Submit Info!", m)
        f3.destroy()
        login(f5)
    except sqlite3.IntegrityError:
        m = "You are alredy register from this Enrollment number"
        messagebox.showerror("Error!", m)

def register(f5):
    global fi1
    global fi2
    fi1.destroy()
    fi2.destroy()

    f3=Frame(root,width=500,height=450,bg="silver",relief=SUNKEN)
    f3.place(x=400,y=100)

    l1=tk.Label(f3,text="Register for Quiz",bd=5,font=("bold",20))
    l1.place(x=150,y=10)

    l2=tk.Label(f3,text="FullName",bd=5,font=("bold",15))
    l2.place(x=50,y=100)
    e1=tk.Entry(f3,font=("bold",15),bd=5,textvariable=h1).place(x=250,y=100)

    l5=tk.Label(f3,text="Email",bd=5,font=("bold",15))
    l5.place(x=50,y=160)
    e6=tk.Entry(f3,font=("bold",15),bd=5,textvariable=h2).place(x=250,y=160)

    l3=tk.Label(f3,text="Enrollment no.",bd=5,font=("bold",15))
    l3.place(x=50,y=220)
    e2=tk.Entry(f3,font=("bold",15),bd=5,textvariable=h3).place(x=250,y=220)

    l4=tk.Label(f3,text="Password",bd=5,font=("bold",15))
    l4.place(x=50,y=280)
    e3=tk.Entry(f3,show="*",font=("bold",15),bd=5,textvariable=h4).place(x=250,y=280)

    logbtn5=tk.Button(f3, text="Register",font=("bold",15),bd=5, command=lambda: okk(f3,f5,e2)).place(x=180,y=350)

#----------------------------------------------------------------------------------------------------------------------------------------------------
#====================================================================================================================================================
#====================================================================================================================================================
#it is only for to add questions or updata the question:

def admini():
    subprocess.run("python adminis.py")
    

def sel(f21):
    global data
    global a
    hh=lan.get()
    if(hh==1):
        data='java.db'
        conn=sqlite3.connect('adimidata.db')
        cursor=conn.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS adimi(data TEXT)')
        cursor.execute('UPDATE adimi SET data=?',(data,))
        conn.commit()
        a=PhotoImage(file="images\\javalogo.PNG")
        f21.destroy()
        f5=Frame(root,width=450,height=300,bg="silver",relief=SUNKEN)
        f5.place(x=400,y=150)
        logbtn11=tk.Button(f5, text="Login",font=("bold",20),bd=5, command=lambda: login(f5)).place(x=100,y=100)
        logbtn12=tk.Button(f5, text="Register",font=("bold",20),bd=5, command=lambda: register(f5)).place(x=250,y=100)
        logbtn13=tk.Button(f5, text="Administrator",font=("bold",20),bd=5, command=admini).place(x=150,y=200)

    elif(hh==2):
        m = "ADMINISTRATOR HAVE NOT UPLOADED THESES QUESTIONS.PLEASE CONTACT"
        messagebox.showerror("Error!", m)
        


    elif(hh==3):
        data='python.db'
        conn=sqlite3.connect('adimidata.db')
        cursor=conn.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS adimi(data TEXT)')
        cursor.execute('UPDATE adimi SET data=?',(data,))
        conn.commit()
        a=PhotoImage(file="images\\pythonlogo.PNG")
        f21.destroy()
        f5=Frame(root,width=450,height=300,bg="silver",relief=SUNKEN)
        f5.place(x=400,y=150)
        logbtn11=tk.Button(f5, text="Login",font=("bold",20),bd=5, command=lambda: login(f5)).place(x=100,y=100)
        logbtn12=tk.Button(f5, text="Register",font=("bold",20),bd=5, command=lambda: register(f5)).place(x=250,y=100)
        logbtn13=tk.Button(f5, text="Administrator",font=("bold",20),bd=5, command=admini).place(x=150,y=200)

    elif(hh==4):
        data='html.db'
        conn=sqlite3.connect('adimidata.db')
        cursor=conn.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS adimi(data TEXT)')
        cursor.execute('UPDATE adimi SET data=?',(data,))
        conn.commit()
        a=PhotoImage(file="images\\htmllogo.PNG")
        f21.destroy()
        f5=Frame(root,width=450,height=300,bg="silver",relief=SUNKEN)
        f5.place(x=400,y=150)
        logbtn11=tk.Button(f5, text="Login",font=("bold",20),bd=5, command=lambda: login(f5)).place(x=100,y=100)
        logbtn12=tk.Button(f5, text="Register",font=("bold",20),bd=5, command=lambda: register(f5)).place(x=250,y=100)
        logbtn13=tk.Button(f5, text="Administrator",font=("bold",20),bd=5, command=admini).place(x=150,y=200)

    else:
        m="Select any Language to play Quiz"
        messagebox.showerror("Error!", m)

def sah(e):
    global b
    global c
    global fi1
    global fi2
    
    k1.destroy()
    
    label=tk.Label(root,text="WELCOME FOR QUIZ",borderwidth=5,bg="silver",font='Arial 25 bold')
    label.place(x=500,y=50)

    fi1=Frame(root,width=300,height=300,bg="silver",bd=5,relief=SUNKEN)
    fi1.place(x=50,y=150)
    b=PhotoImage(file="images\\aa1.PNG")

    label=tk.Label(fi1,image=b,borderwidth=5,bg="silver",font='Arial 25 bold')
    label.place(x=0,y=0)

    fi2=Frame(root,width=300,height=300,bg="silver",bd=5,relief=SUNKEN)
    fi2.place(x=900,y=150)
    
    c=PhotoImage(file="images\\aa2.PNG")

    label=tk.Label(fi2,image=c,borderwidth=5,bg="silver",font='Arial 25 bold')
    label.place(x=0,y=0)



    f21=Frame(root,width=450,height=350,bg="silver",bd=5,relief=SUNKEN)
    f21.place(x=400,y=150)

    label=tk.Label(f21,text="Select Your Language",bd=5,font=("bold",20))
    label.place(x=80,y=15)

    rbf21=Radiobutton(f21,text="JAVA",variable=lan,value=1,bd=5,width=8,font=("bold",15))
    rbf21.place(x=70,y=100)

    rbf22=Radiobutton(f21,text="C++",variable=lan,value=2,width=8,bd=5,font=("bold",15))
    rbf22.place(x=240,y=100)

    rbf23=Radiobutton(f21,text="PYTHON",variable=lan,value=3,width=8,bd=5,font=("bold",15))
    rbf23.place(x=70,y=180)

    rbf24=Radiobutton(f21,text="HTML",variable=lan,value=4,width=8,bd=5,font=("bold",15))
    rbf24.place(x=240,y=180)

    logbtn5=tk.Button(f21, text="Select Language",font=("bold",15),bd=5, command=lambda: sel(f21)).place(x=120,y=250)

#b=PhotoImage(file="F:\\python project\\images\\aa1.PNG")



k1=Frame(root,width=1450,height=800,bg="antiquewhite2")
k1.place(x=10,y=10)
a=PhotoImage(file="images\\my_image.PNG")
global l
l=Label(k1,image=a,width=300,height=300)
l.place(x=200,y=120)

y=PhotoImage(file="images\\aa4.PNG")
ll2=Label(k1,image=y,width=600,height=200)
ll2.place(x=50,y=450)

l.bind('<Motion>',sah)
Label(k1,text="!!WELCOME!!",relief="ridge",font='courier 50 bold',bg="silver").place(x=500,y=20)
Label(k1,text="NAME:-ABHAY SAHU",relief="ridge",font='courier 20 bold',bg="lightblue").place(x=700,y=200)
Label(k1,text="ERNO.:-171B005",relief="ridge",font='courier 20 bold',bg="lightblue").place(x=700,y=300)
Label(k1,text="BATCH:-B1",relief="ridge",font='courier 20 bold',bg="lightblue").place(x=700,y=400)
Label(k1,text="EMAIL:-sahua545@gmail.com",relief="ridge",font='courier 20 bold',bg="lightblue").place(x=700,y=500)
Label(k1,text="CONTACT No.:-9617625945",relief="ridge",font='courier 20 bold',bg="lightblue").place(x=700,y=600)


root.mainloop()


# In[ ]:




