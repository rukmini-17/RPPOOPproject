#DIGITAL ATTENDANCE MANAGEMENT SYSTEM
'''
DATABASE : rppoop_ams.db
1. Table1: student_data
2. Table2: Attendance
'''    

from tkinter import*
import sqlite3
import pandas as pd


#Globals and Macros
ADMINPASSWORD = 'abc'
excel_output = []

#Extra functions
def convertTuple(tup):
    str = ''
    if tup == None:
        return "None"
    for item in tup:
        str = str + item
    return str


def import_from_excel():
    df = pd.read_excel('data.xlsx')
    temp = []
    for i in range(0,3):
        list1 = df.loc[i]
        temp.append(list(list1))

    
    for list2 in temp:
        temp2 = [str(x) for x in list2]
        excel_output.append(temp2)


#SQL CONNECTION 
mydb = sqlite3.connect("rppoop_ams.db")
cur = mydb.cursor()


#For LOGIN BUTTON 
def get_input():

    enrollmentNo = e1.get()   #e1 = enrollment entry box
    password = e2.get()       #e2 = password entry box

    #check if both entries are filled
    if enrollmentNo == '' or password == '':
        r=Tk()
        r.configure(background='white')
        Label(r,text='ENTER DATA!',fg='red',bg='white').pack(fill=X)
        Button(r,text='Okay',fg='blue',bg='white',command=r.destroy).pack(fill=X)
        r.mainloop()

    #get EnrollmentNo from student_data into enrollList
    cur.execute("select EnrollmentNo from student_data")
    enrollList = [item for tuple in cur.fetchall() for item in tuple]   

    #Wrong EnrollmentNo condition
    if enrollmentNo not in enrollList:
        e1.delete(0,END)
        e2.delete(0,END)
        r=Tk()
        r.configure(background='white')
        Label(r,text='INVALID ENROL NO. OR PASSWORD !',fg='red',bg='white').pack()
        Button(r,text='Okay',bg='white',command=r.destroy).pack()
        r.mainloop()

    #select password of student
    cur.execute("select password from student_data where EnrollmentNo = {var}".format(var = enrollmentNo))
    pwd = convertTuple(cur.fetchone())

    #Wrong password condition
    if enrollmentNo in enrollList and password != pwd:
        e2.delete(0,END)
        wrong=Tk()
        wrong.configure(background='white')
        l=Label(wrong,text='WRONG PASSWORD ENTERED!!!\nENTER PASSWORD AGAIN.',fg='red',bg='white',font='times,5').pack()
        k=Button(wrong,text='Okay',fg='blue',bg='white',command=wrong.destroy).pack()
        wrong.mainloop()
    
    #ENROLLMENTNO AND PASSWORD VERIFIED!!
    e1.delete(0,END)
    e2.delete(0,END)
    
    #<<<<<<<<<<<<<<<<<<<<<<<<PROFILE WINDOW>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    
    #select the logged in student
    cur.execute("select name from student_data where EnrollmentNo = {var}".format(var = enrollmentNo))
    name = convertTuple(cur.fetchone()) 
    
    profile=Tk()
    profile.configure(background='white')
    profile.title('Student Profile')
    l=Label(profile,text='WELCOME '+ name.upper() + ' !',fg='blue',bg='white',font=('Times New Roman',8,'bold')).grid(row=0,column=2)
    
    #get Date data
    cur.execute("select date from Attendance")
    templist = [item for tuple in cur.fetchall() for item in tuple]
    datelist = list(set(templist))
    datelist.sort()

    k = len(datelist)   #no of dates
    
    #create listboxes for date and PCM attendances
    list_date=Listbox(profile,height=k)
    list_P=Listbox(profile,width=20,height=k)
    list_C=Listbox(profile,height=k)
    list_M=Listbox(profile,height=k)
    list_P.insert(1,'PHYSICS')
    list_P.itemconfig(0,{'fg':'orange'})
    list_C.insert(1,'CHEMISTRY')
    list_C.itemconfig(0,{'fg':'orange'})
    list_M.insert(1,'MATHS')
    list_M.itemconfig(0,{'fg':'orange'})
    
    #date output
    for j1 in range(0,k):
        list_date.insert(j1+1,datelist[j1])
        list_date.itemconfig(j1,{'fg':'blue'})

    #physics attendace output
    cur.execute("select Physics from Attendance")
    pa = [item for tuple in cur.fetchall() for item in tuple]   
    
    for j2 in range(0,k):
        list_P.insert(j2+1,pa[j2])
        if pa[j2] =='P':
            list_P.itemconfig(j2+1,{'fg':'green'})
        elif pa[j2] =='A':
            list_P.itemconfig(j2+1,{'fg':'red'})
    
    #chemistry attendance output
    cur.execute("select Chemistry from Attendance")
    ca = [item for tuple in cur.fetchall() for item in tuple] 

    for j3 in range(0,k):
        list_C.insert(j3+1,ca[j3])
        if ca[j3]=='P':
            list_C.itemconfig(j3+1,{'fg':'green'})
        elif ca[j3]=='A':
            list_C.itemconfig(j3+1,{'fg':'red'})
    
    #maths attendance output
    cur.execute("select Maths from Attendance")
    ma = [item for tuple in cur.fetchall() for item in tuple] 

    for j4 in range(0,k):
        list_M.insert(j4+1,ma[j4])
        if ma[j4]=='P':
            list_M.itemconfig(j4+1,{'fg':'green'})
        elif ma[j4]=='A':
            list_M.itemconfig(j4+1,{'fg':'red'})

    #GUI stuff
    list_date.grid(row=1,column=1)  
    list_P.grid(row=1,column=2) 
    list_C.grid(row=1,column=3)
    list_M.grid(row=1,column=4)
    
    #calculating attendance percentage
    p1=str(pa.count('P'))
    p2=str(ca.count('P'))
    p3=str(ma.count('P'))
    a1=str(pa.count('A'))
    a2=str(ca.count('A'))
    a3=str(ma.count('A'))
    
    atdPt=float((int(p1)/(int(p1)+int(a1)))*100) 
    atdCt=float((int(p2)/(int(p2)+int(a2)))*100)
    atdMt=float((int(p3)/(int(p3)+int(a3)))*100)
    atdP=str(round(atdPt,2))
    atdC=str(round(atdCt,2))
    atdM=str(round(atdMt,2))
    
    #GUI stuff
    Label(profile,text='TRY NOT TO',fg='red',bg='white',width=18).grid(row=2,column=1)
    Label(profile,text='MISS LECTURES.',fg='red',bg='white',width=18).grid(row=3,column=1)
    Button(profile,bg='white',fg='navy blue',text='LOG OUT',font=('helventica',8,'bold'),width=18,command=profile.destroy).grid(row=4,column=1)
    Label(profile,text='Total P='+p1,bg='white',width=18,fg='magenta').grid(row=2,column=2)
    Label(profile,text='Total A='+a1,bg='white',width=18,fg='purple').grid(row=3,column=2)
    Label(profile,text='Total P='+p2,bg='white',width=18,fg='magenta').grid(row=2,column=3)
    Label(profile,text='Total A='+a2,bg='white',width=18,fg='purple').grid(row=3,column=3)
    Label(profile,text='Total P='+p3,bg='white',width=18,fg='magenta').grid(row=2,column=4)
    Label(profile,text='Total A='+a3,bg='white',width=18,fg='purple').grid(row=3,column=4)
    Label(profile,text='Attendance='+atdP+'%',bg='black',width=18,fg='white').grid(row=4,column=2)
    Label(profile,text='Attendance='+atdC+'%',bg='black',width=18,fg='white').grid(row=4,column=3)
    Label(profile,text='Attendance='+atdM+'%',bg='black',width=18,fg='white').grid(row=4,column=4)
        
    profile.mainloop()

#FOR EXIT BUTTON (DONE)
def quitroot():
    qroot=Tk()
    qroot.configure(background='white')
    Label(qroot,text='Are You Sure You Want To Exit ?',fg='red',bg='white',font=('Times',12,'bold')).pack(side=TOP)
    Button(qroot,text='NO',fg='blue',bg='white',command=qroot.destroy).pack(side=BOTTOM)
    def destroyall():
        qroot.destroy()
        root.destroy()
    Button(qroot,text='YES',fg='blue',bg='white',command=destroyall).pack(side=BOTTOM)
    qroot.mainloop()

#FOR SIGNUP BUTTON  (DONE)
def sign_up():
    #signup_window GUI
    signup_window=Tk() 
    signup_window.configure(background='white')
    signup_window.title('NEW ENTRY')  
    signup_window.geometry('400x400') 

    l1=Label(signup_window,text=' NAME :',fg='blue',bg='white',font=('Times New Roman',10)).place(relx=0.3,rely=0.2,anchor=CENTER)
    n1=Entry(signup_window)
    n1.place(relx=0.6,rely=0.2,anchor=CENTER)

    l2=Label(signup_window,text='ENROLMENT NO :',fg='blue',bg='white',font=('Times New Roman',10)).place(relx=0.25,rely=0.37,anchor=CENTER) 
    n2=Entry(signup_window)
    n2.place(relx=0.6,rely=0.37,anchor=CENTER)

    l3=Label(signup_window,text='        PASSWORD :',fg='blue',bg='white',font=('Times New Roman',10)).place(relx=0.25,rely=0.55,anchor=CENTER)
    n3=Entry(signup_window,show='*')
    n3.place(relx=0.6,rely=0.55,anchor=CENTER)

    l4=Label(signup_window,text='CONFIRM PASSWORD :',fg='blue',bg='white',font=('Times New Roman',10)).place(relx=0.220,rely=0.7,anchor=CENTER)
    n4=Entry(signup_window,show='*')
    n4.place(relx=0.6,rely=0.7,anchor=CENTER)

    #function for saving new entry (called onclick: SAVE button)
    def save_new():
        #get EnrollmentNo from student_data into enrollList
        cur.execute("select EnrollmentNo from student_data")
        enrollList1 = [item for tuple in cur.fetchall() for item in tuple]
          
        #if all fields are not filled ask user to fill them
        if n1.get()=='' or n2.get()=='' or n3.get()=='' or n4.get()=='': 
            v=Tk()
            v.configure(background='white')
            n=Label(v,text='ENTER DATA!',fg='red',bg='white',font='times,4').pack()
            d=Button(v,text='OKAY',fg='blue',bg='white',command=v.destroy).pack()
            v.mainloop()
        
        #if the enrollmentNo already exists don't make a new entry
        elif any((n1.get()) in s for s in enrollList1): 
            def clear_data():
                q.destroy()
                n1.delete(0,END)
                n2.delete(0,END)
                n3.delete(0,END)
                n4.delete(0,END)
            
            q=Tk()
            q.configure(background='white')
            l=Label(q,text='Data Already Exists!',fg='red',font='times,6').pack()
            but=Button(q,text='Okay',fg='blue',bg='white',command=clear_data).pack()
            q.mainloop()
        
        #Insert data of new student
        else: 
            #Insert into database
            s = "insert into student_data(EnrollmentNo,name,password) values(?,?,?)"
            b1 = (n2.get(),n1.get(),n3.get())
            cur.execute(s,b1)
            mydb.commit()

            #delete entries
            n1.delete(0,END) 
            n2.delete(0,END)
            n3.delete(0,END)
            n4.delete(0,END)

            q=Tk()
            q.configure(background='white')
            L=Label(q,text='Entry Saved',fg='green',bg='white',font='helventica,5').pack()
            B=Button(q,text='Okay',fg='blue',bg='white',font='times,3',command=q.destroy).pack()
            q.mainloop()
    
    #SAVE button
    b1 = Button(signup_window,text='SAVE',command=save_new,fg='red',bg='white',font=('Helventica',8)).place(relx=0.5,rely=0.85,anchor=CENTER)                              
          
    signup_window.mainloop()  

      
#FOR ADMIN LOGIN 
def date_supply():
    date=Tk()
    date.title('date entry')
    date.configure(background='white')
    date.geometry('300x300')
    Label(date, text='Enter date in DD|MM|YY format: ', fg='black', bg= 'white', font=('calibri', 13)).pack(side=TOP)
    Datelabel=Label(date, text=' DD: ', fg='black', bg='white', font=('calibri', 10)).place(relx=0.2, rely=0.2, anchor=CENTER)
    Dateentry=Entry(date, bg= 'white', fg='black', relief=SUNKEN)
    Dateentry.place(relx=0.6, rely= 0.2, anchor=CENTER)

    monthlabel=Label(date, text=' MM: ', fg='black', bg='white', font=('calibri', 10)).place(relx=0.2, rely=0.4, anchor=CENTER)
    monthentry=Entry(date, bg= 'white', fg='black', relief=SUNKEN)
    monthentry.place(relx=0.6, rely= 0.4, anchor=CENTER)

    yearlabel=Label(date, text=' YY: ', fg='black', bg='white', font=('calibri', 10)).place(relx=0.2, rely=0.6, anchor=CENTER)
    yearentry=Entry(date, bg= 'white', fg='black', relief=SUNKEN)
    yearentry.place(relx=0.6, rely= 0.6, anchor=CENTER)

    cur.execute("select date from Attendance")
    templist = [item for tuple in cur.fetchall() for item in tuple]
    dates = list(set(templist))
    dates.sort()

    def save_date():
        dd=Dateentry.get()
        mm=monthentry.get()
        yy=yearentry.get()
        global date_record
        date_record = "{dd}|{mm}|{yy}".format(dd=dd,mm=mm,yy=yy)
        if date_record in dates:
            wrong_date=Tk()
            wrong_date.configure(background='white')
            Label(wrong_date,text='DATE ALREADY PRESENT!',fg='red',bg='white',font=('Times',12,'bold')).pack(fill=X)
            Button(wrong_date,text='Okay',bg='white',command=wrong_date.destroy).pack(fill=X)
            Dateentry.delete(0,END)
            monthentry.delete(0,END)
            yearentry.delete(0,END)
        
        else:

            cur.execute("select enrollmentNo from student_data")
            enrollList = [item for tuple in cur.fetchall() for item in tuple]

            cur.execute("select name from student_data")
            namelist = [item for tuple in cur.fetchall() for item in tuple]

            cmd = "insert into Attendance(EnrollmentNo,name,date,Physics,Chemistry,Maths) values(?,?,?,?,?,?)"

            for i in range(0,len(enrollList)):
                print("done")
                data = (enrollList[i],namelist[i],date_record,"NA","NA","NA")
                cur.execute(cmd,data)
                mydb.commit()
            
            correct_date=Tk()
            correct_date.configure(background='white')
            Label(correct_date,text='DATE SAVED!',fg='green',bg='white',font=('Times',12,'bold')).pack(fill=X)
            Button(correct_date,text='Okay',bg='white',command=correct_date.destroy).pack(fill=X)
            
            date.destroy()


    dateb=Button(date,text='SAVE',font=('calibri',11),fg='white',bg='black',command=save_date).place(relx=0.5,rely=0.8,anchor=CENTER)
    date.mainloop()

    
    #return date_record


def admin_login():
    def admin_view():
        if admin_pwd.get()==ADMINPASSWORD:   
            adminLogin_window.destroy()
            admin_menu=Tk()
            admin_menu.configure(background='white')
            admin_menu.title('ADMIN')
            Label(admin_menu,text='CHOOSE LECTURE :',fg='purple',bg='white',font=('Times New Roman',25)).pack(fill=X)
            
            def phy_atd():
                
                check = date_record

                cur.execute("select date from Attendance")
                templist = [item for tuple in cur.fetchall() for item in tuple]
                dates = list(set(templist))
                dates.sort()

                cur.execute("select name from student_data")
                a = [item for tuple in cur.fetchall() for item in tuple]
                
                phy=Tk()
                phy.title('PHYSICS')
                phy.configure(background='white')
                lb1=Listbox(phy,width=2,font='times,1',height=len(a))
                lb1.pack(side=LEFT)
                lb2=Listbox(phy,fg='blue',selectmode=EXTENDED,width=16,font='times,1',height=len(a))
                lb2.pack(side=LEFT)
                i=0
                for name in a:
                    i+=1
                    lb1.insert(i,str(i)+'.')
                    lb2.insert(i,name)
                Label(phy,text='P/A',bg='white',font='times,0.1').pack(side=TOP)
                entries=[]        #list of P/A for that date namewise (has tkinter object)
                for i in range(len(a)):
                    e=Entry(phy,width=3)
                    e.pack(side=TOP)
                    entries.append(e)    
                def update_data():
                    sa=[]    
                    for k in entries:
                        sa.append(k.get())
                    def echeck():           #checking if all entries are either P or A
                        for n in sa:
                            if n=='P' or n=='A':
                                ec=0
                            else:
                                ec=1
                                break
                        return(ec)    
                    
                    if '' in sa:
                            temp=Tk()
                            temp.configure(background='white')
                            Label(temp,text='Please fill all the entries !',fg='red',bg='white',font='times,4').pack()
                            Button(temp,text='Okay',bg='white',command=temp.destroy).pack()
                            temp.mainloop()
                    elif echeck()==1:
                            wrong_entry=Tk()
                            wrong_entry.configure(background='white')
                            Label(wrong_entry,text='Fill either P or A',fg='blue',bg='white').pack()
                            Button(wrong_entry,text='Okay',fg='red',bg='white',command=wrong_entry.destroy).pack()
                            wrong_entry.mainloop()  

                    else:
                        psure=Tk()
                        psure.configure(background='white')
                        Label(psure,text='ARE YOU SURE ?\nDID YOU CHECK ALL THE ENTRIES ?',fg='red',bg='white').pack()
                        Button(psure,text='NO',fg='blue',bg='white',command=psure.destroy).pack()

                        def p_sure():
                            psure.destroy()   

                            cur.execute("select enrollmentNo from student_data")
                            enrollList3 = [item for tuple in cur.fetchall() for item in tuple]

                            for i in range(0,len(entries)):
                                cur.execute("update attendance set physics = '{sa}' where enrollmentNo = '{enroll}' and date = '{date}'".format(sa = sa[i],enroll = enrollList3[i],date = check))
                                mydb.commit()
                            phy.destroy()

                        Button(psure,text='YES',fg='blue',bg='white',command=p_sure).pack()
                        psure.mainloop()               
                            
                Button(phy,text='UPDATE DATA',fg='red',bg='white',command=update_data).pack()
                phy.mainloop()
                              
            def chem_atd():
                check = date_record
                cur.execute("select date from Attendance")
                templist = [item for tuple in cur.fetchall() for item in tuple]
                dates = list(set(templist))
                dates.sort()
               
                cur.execute("select name from student_data")
                a = [item for tuple in cur.fetchall() for item in tuple]
                chm=Tk()
                chm.title('CHEMISTRY')
                chm.configure(background='white')
                lb1=Listbox(chm,width=2,font='times,1',height=len(a))
                lb1.pack(side=LEFT)
                lb2=Listbox(chm,fg='blue',selectmode=EXTENDED,width=16,font='times,1',height=len(a))
                lb2.pack(side=LEFT)
                i=0
                for name in a:
                    i+=1
                    lb1.insert(i,str(i)+'.')
                    lb2.insert(i,name)
                Label(chm,text='P/A',bg='white',font='times,0.1').pack(side=TOP)
                entries=[]        #list of P/A for that date namewise (has tkinter object)
                for i in range(len(a)):
                    e=Entry(chm,width=3)
                    e.pack(side=TOP)
                    entries.append(e)    
                def update_data():
                    sa=[]    
                    for k in entries:
                        sa.append(k.get())
                    def echeck():           #checking if all entries are either P or A
                        for n in sa:
                            if n=='P' or n=='A':
                                ec=0
                            else:
                                ec=1
                                break
                        return(ec)    
                    
                    if '' in sa:
                        temp=Tk()
                        temp.configure(background='white')
                        Label(temp,text='Please fill all the entries !',fg='red',bg='white',font='times,4').pack()
                        Button(temp,text='Okay',bg='white',command=temp.destroy).pack()
                        temp.mainloop()
                    elif echeck()==1:
                        wrong_entry=Tk()
                        wrong_entry.configure(background='white')
                        Label(wrong_entry,text='Fill either P or A',fg='blue',bg='white').pack()
                        Button(wrong_entry,text='Okay',fg='red',bg='white',command=wrong_entry.destroy).pack()
                        wrong_entry.mainloop()  

                    else:
                        csure=Tk()
                        csure.configure(background='white')
                        Label(csure,text='ARE YOU SURE ?\nDID YOU CHECK ALL THE ENTRIES ?',fg='red',bg='white').pack()
                        Button(csure,text='NO',fg='blue',bg='white',command=csure.destroy).pack()

                        def c_sure():
                            csure.destroy()   

                            cur.execute("select enrollmentNo from student_data")
                            enrollList3 = [item for tuple in cur.fetchall() for item in tuple]

                            for i in range(0,len(entries)):
                                cur.execute("update attendance set chemistry = '{sa}' where enrollmentNo = '{enroll}' and date = '{date}'".format(sa = sa[i],enroll = enrollList3[i],date = check))
                                mydb.commit()
                            chm.destroy()

                        Button(csure,text='YES',fg='blue',bg='white',command=c_sure).pack()
                        csure.mainloop()                
                            
                Button(chm,text='UPDATE DATA',fg='red',bg='white',command=update_data).pack()
                chm.mainloop()
      
            def mat_atd():
                check = date_record
                cur.execute("select date from Attendance")
                templist = [item for tuple in cur.fetchall() for item in tuple]
                dates = list(set(templist))
                dates.sort()
               
                cur.execute("select name from student_data")
                a = [item for tuple in cur.fetchall() for item in tuple]
                mat=Tk()
                mat.title('MATHS')
                mat.configure(background='white')
                lb1=Listbox(mat,width=2,font='times,1',height=len(a))
                lb1.pack(side=LEFT)
                lb2=Listbox(mat,fg='blue',selectmode=EXTENDED,width=16,font='times,1',height=len(a))
                lb2.pack(side=LEFT)
                i=0
                for name in a:
                    i+=1
                    lb1.insert(i,str(i)+'.')
                    lb2.insert(i,name)
                Label(mat,text='P/A',bg='white',font='times,0.1').pack(side=TOP)
                entries=[]        #list of P/A for that date namewise (has tkinter object)
                for i in range(len(a)):
                    e=Entry(mat,width=3)
                    e.pack(side=TOP)
                    entries.append(e)    
                def update_data():
                    sa=[]    
                    for k in entries:
                        sa.append(k.get())
                    def echeck():           #checking if all entries are either P or A
                        for n in sa:
                            if n=='P' or n=='A':
                                ec=0
                            else:
                                ec=1
                                break
                        return(ec)    
                    
                    if '' in sa:
                        temp=Tk()
                        temp.configure(background='white')
                        Label(temp,text='Please fill all the entries !',fg='red',bg='white',font='times,4').pack()
                        Button(temp,text='Okay',bg='white',command=temp.destroy).pack()
                        temp.mainloop()
                    elif echeck()==1:
                        wrong_entry=Tk()
                        wrong_entry.configure(background='white')
                        Label(wrong_entry,text='Fill either P or A',fg='blue',bg='white').pack()
                        Button(wrong_entry,text='Okay',fg='red',bg='white',command=wrong_entry.destroy).pack()
                        wrong_entry.mainloop()  

                    else:
                        msure=Tk()
                        msure.configure(background='white')
                        Label(msure,text='ARE YOU SURE ?\nDID YOU CHECK ALL THE ENTRIES ?',fg='red',bg='white').pack()
                        Button(msure,text='NO',fg='blue',bg='white',command=msure.destroy).pack()

                        def m_sure():
                            msure.destroy()   

                            cur.execute("select enrollmentNo from student_data")
                            enrollList3 = [item for tuple in cur.fetchall() for item in tuple]

                            for i in range(0,len(entries)):
                                cur.execute("update attendance set maths = '{sa}' where enrollmentNo = '{enroll}' and date = '{date}'".format(sa = sa[i],enroll = enrollList3[i],date = check))
                                mydb.commit()
                            mat.destroy()

                        Button(msure,text='YES',fg='blue',bg='white',command=m_sure).pack()
                        msure.mainloop()                
                            
                Button(mat,text='UPDATE DATA',fg='red',bg='white',command=update_data).pack()
                mat.mainloop()

            def see_atd():
                see=Tk()
                see.configure(background='white')
                see.title('ATTENDANCE DATA')
                Label(see,text='PHY',fg='blue',bg='white',font=('Comic',12,'bold')).grid(row=0,column=1)
                Label(see,text='CHEM',fg='blue',bg='white',font=('Comic',12,'bold')).grid(row=2,column=1)
                Label(see,text='MATHS',fg='blue',bg='white',font=('Comic',12,'bold')).grid(row=4,column=1)
                names1=Listbox(see)
                names1.insert(1,'NAMES')
                names1.itemconfig(0,{'fg':'red'})
                enrol1=Listbox(see,width=10)
                enrol1.insert(1,'ENROL NO.')
                enrol1.itemconfig(0,{'fg':'Purple'})
                attendance1=Listbox(see,width=187)
                
                names2=Listbox(see)
                names2.insert(1,'NAMES')
                names2.itemconfig(0,{'fg':'red'})
                enrol2=Listbox(see,width=10)
                enrol2.insert(1,'ENROL NO.')
                enrol2.itemconfig(0,{'fg':'Purple'})
                attendance2=Listbox(see,width=187)
                
                names3=Listbox(see)
                names3.insert(1,'NAMES')
                names3.itemconfig(0,{'fg':'red'})
                enrol3=Listbox(see,width=10)
                enrol3.insert(1,'ENROL NO.')
                enrol3.itemconfig(0,{'fg':'Purple'})
                attendance3=Listbox(see,width=187)
                

                cur.execute("select name from student_data")
                namelist = [item for tuple in cur.fetchall() for item in tuple]
                length = len(namelist)

                cur.execute("select enrollmentNo from student_data")
                enrollList = [item for tuple in cur.fetchall() for item in tuple]
                   
                
                for i in range(0,length):
                    names1.insert(i+1,namelist[i])
                    enrol1.insert(i+1,enrollList[i])
                    names2.insert(i+1,namelist[i])
                    enrol2.insert(i+1,enrollList[i])
                    names3.insert(i+1,namelist[i])
                    enrol3.insert(i+1,enrollList[i])
                    names1.itemconfig(i,{'fg':'navy blue'})
                    names2.itemconfig(i,{'fg':'navy blue'})
                    names3.itemconfig(i,{'fg':'navy blue'})
                    enrol1.itemconfig(i,{'fg':'Orange'})
                    enrol2.itemconfig(i,{'fg':'Orange'})
                    enrol3.itemconfig(i,{'fg':'Orange'})
                

                cur.execute("select date from Attendance")
                templist = [item for tuple in cur.fetchall() for item in tuple]
                dates = list(set(templist))
                dates.sort()
                   
                attendance1.insert(1,dates)
                attendance2.insert(1,dates)
                attendance3.insert(1,dates)

                #Physics attendance update
                for i in range(1,length+1):
                    temp1 = []
                    cur.execute("select physics from attendance where name = '{var}' ".format(var = namelist[i-1]))
                    temp1 = [item for tuple in cur.fetchall() for item in tuple]
                    temp2 = []
                    for j in range(0,len(temp1)):
                        temp2.append('______' + temp1[j])
                    attendance1.insert(i+1,temp2)
                    attendance1.itemconfig(i,{'fg':'Blue'})

                #chemistry attendance update
                for i in range(1,length+1):
                    temp1 = []
                    cur.execute("select chemistry from attendance where name = '{var}' ".format(var = namelist[i-1]))
                    temp1 = [item for tuple in cur.fetchall() for item in tuple]
                    temp2 = []
                    for j in range(0,len(temp1)):
                        temp2.append('______' + temp1[j])
                    attendance2.insert(i+1,temp2)
                    attendance2.itemconfig(i,{'fg':'Blue'})
    
                #maths attendance update
                for i in range(1,length+1):
                    temp1 = []
                    cur.execute("select maths from attendance where name = '{var}' ".format(var = namelist[i-1]))
                    temp1 = [item for tuple in cur.fetchall() for item in tuple]
                    temp2 = []
                    for j in range(0,len(temp1)):
                        temp2.append('______' + temp1[j])
                    attendance3.insert(i+1,temp2)
                    attendance3.itemconfig(i,{'fg':'Blue'})
     
                names1.grid(row=1,column=0)
                enrol1.grid(row=1,column=1)
                attendance1.grid(row=1,column=2)
                names2.grid(row=3,column=0)
                enrol2.grid(row=3,column=1)
                attendance2.grid(row=3,column=2)
                names3.grid(row=5,column=0)
                enrol3.grid(row=5,column=1)
                attendance3.grid(row=5,column=2)
                def logout():
                    see.destroy()
                    admin_menu.destroy()
                Button(see,text='LOG OUT',fg='blue',bg='white',font=('Helventica',10,'bold'),command=logout).grid(row=6,column=1)
                Button(see,text='CLOSE',fg='red',bg='white',font=('Helventica',10,'bold'),command=see.destroy).grid(row=6,column=0)
                Label(see,text='N = NOT AVAILABLE',fg='red').grid(row=6,column=2)
                see.mainloop()

            def upload():
                import_from_excel()
                #export data from list to database
                for item in excel_output:
                    cmd = "insert into student_data(EnrollmentNo,name,password) values(?,?,?)"
                    b = (item[0],item[1],item[2])
                    cur.execute(cmd,b)
                    mydb.commit()
                #confirmation window
                upload_success=Tk()
                upload_success.configure(background='white')
                Label(upload_success,text='Data uploaded successfully from data.xlsx',fg='green',bg='white',font=('Times',12,'bold')).pack(fill=X)
                Button(upload_success,text='Okay',bg='white',command=upload_success.destroy).pack(fill=X)
                
            #these functions should generate a PDF report of attendance for a particular subject
            def phy_report():
                cur.execute("select name from student_data")
                namelist = [item for tuple in cur.fetchall() for item in tuple]
                length = len(namelist)

                cur.execute("select enrollmentNo from student_data")
                enrollList = [item for tuple in cur.fetchall() for item in tuple]

                cur.execute("select date from Attendance")
                templist = [item for tuple in cur.fetchall() for item in tuple]
                dates = list(set(templist))
                dates.sort()

                phy_attend = []
                
                for i in range(0,length):
                    temp1 = []
                    cur.execute("select physics from attendance where name = '{var}' ".format(var = namelist[i]))
                    temp1 = [item for tuple in cur.fetchall() for item in tuple]
                    phy_attend.append(temp1)

                #BELOW THIS: TO BE DONE BY RUKMINI
                #you have 4 lists - enrollList, namelist, dates, phy_attend
                #make a pdf report out if it

            def chem_report():
                cur.execute("select name from student_data")
                namelist = [item for tuple in cur.fetchall() for item in tuple]
                length = len(namelist)

                cur.execute("select enrollmentNo from student_data")
                enrollList = [item for tuple in cur.fetchall() for item in tuple]

                cur.execute("select date from Attendance")
                templist = [item for tuple in cur.fetchall() for item in tuple]
                dates = list(set(templist))
                dates.sort()

                chem_attend = []
                
                for i in range(0,length):
                    temp1 = []
                    cur.execute("select chemistry from attendance where name = '{var}' ".format(var = namelist[i]))
                    temp1 = [item for tuple in cur.fetchall() for item in tuple]
                    chem_attend.append(temp1)

                #BELOW THIS: TO BE DONE BY RUKMINI
                #you have 4 lists - enrollList, namelist, dates, chem_attend
                #make a pdf report out if it

            def mat_report():
                cur.execute("select name from student_data")
                namelist = [item for tuple in cur.fetchall() for item in tuple]
                length = len(namelist)

                cur.execute("select enrollmentNo from student_data")
                enrollList = [item for tuple in cur.fetchall() for item in tuple]

                cur.execute("select date from Attendance")
                templist = [item for tuple in cur.fetchall() for item in tuple]
                dates = list(set(templist))
                dates.sort()

                mat_attend = []
                
                for i in range(0,length):
                    temp1 = []
                    cur.execute("select maths from attendance where name = '{var}' ".format(var = namelist[i]))
                    temp1 = [item for tuple in cur.fetchall() for item in tuple]
                    mat_attend.append(temp1)

                #BELOW THIS: TO BE DONE BY RUKMINI
                #you have 4 lists - enrollList, namelist, dates, mat_attend
                #make a pdf report out if it

            def generate_report():
                gen_report_window=Tk()
                gen_report_window.configure(background='white')
                b1=Button(gen_report_window,text='PHYSICS',fg='white',bg='aquamarine',font=('Verdana',16,'bold'),height=5,width=8,command=phy_report)
                b1.pack(fill=X)
                b2=Button(gen_report_window,text='CHEMISRY',fg='white',bg='turquoise',font=('Verdana',16,'bold'),height=5,width=8,command=chem_report)
                b2.pack(fill=X)
                b3=Button(gen_report_window,text='MATHS',fg='white',bg='lightseagreen',font=('Verdana',16,'bold'),height=5,width=8,command=mat_report)
                b3.pack(fill=X) 

            b0=Button(admin_menu,text='SELECT DATE',fg='black',bg='lightgrey',font=('times',16,'bold'),height=4,width=8,command=date_supply)
            b0.pack(fill=X)
            b1=Button(admin_menu,text='PHYSICS',fg='white',bg='aquamarine',font=('Verdana',16,'bold'),height=4,width=8,command=phy_atd)
            b1.pack(fill=X)
            b2=Button(admin_menu,text='CHEMISRY',fg='white',bg='turquoise',font=('Verdana',16,'bold'),height=4,width=8,command=chem_atd)
            b2.pack(fill=X)
            b3=Button(admin_menu,text='MATHS',fg='white',bg='lightseagreen',font=('Verdana',16,'bold'),height=4,width=8,command=mat_atd)
            b3.pack(fill=X)        
            b4=Button(admin_menu,text='SEE ATTENDANCE',fg='black',bg='lightgrey',font=('times',16,'bold'),height=4,width=8,command=see_atd)
            b4.pack(fill=X)
            b5=Button(admin_menu,text='UPLOAD DATA',fg='black',bg='lightgrey',font=('times',16,'bold'),height=4,width=8,command=upload)
            b5.pack(fill=X)
            b5=Button(admin_menu,text='GENERATE REPORT',fg='black',bg='lightgrey',font=('times',16,'bold'),height=4,width=8,command=generate_report)
            b5.pack(fill=X)
            admin_menu.mainloop()
        else:
            admin_pwd.delete(0,END)
            wrong_pwd=Tk()
            wrong_pwd.configure(background='white')
            Label(wrong_pwd,text='Wrong Password!',fg='red',bg='white',font=('Times',12,'bold')).pack(fill=X)
            Button(wrong_pwd,text='Okay',bg='white',command=wrong_pwd.destroy).pack(fill=X)
             
    adminLogin_window=Tk()
    adminLogin_window.configure(background='white')
    Label(adminLogin_window,text='ENTER PASSWORD :',fg='purple',bg='white',font=('Times New Roman',13,'bold italic')).pack()
    admin_pwd=Entry(adminLogin_window,show='*',fg='magenta')
    admin_pwd.pack()
    Button(adminLogin_window,text='LOGIN',fg='blue',bg='white',command=admin_view).pack()
    adminLogin_window.mainloop()

#Main window
root=Tk()
root.title('STUDENT LOGIN')

#specify the path for background pic to be used
bgpic = PhotoImage(file="bg_image.png")
bglabel = Label(root,image=bgpic)
bglabel.pack(fill=Y)

#GUI
w1=Label(root,text='Enrollment No :',fg='red',bg='white',font=('Times New Roman',13,'bold')).place(relx=0.35,rely=0.36,anchor=CENTER)
e1=Entry(root,bg="white",fg="black",relief=SUNKEN)
e1.place(relx=0.48,rely=0.36,anchor=CENTER)
w2=Label(root,text='      Password :',fg='red',bg='white',font=('Times New Roman',13,'bold')).place(relx=0.35,rely=0.45,anchor=CENTER)
e2=Entry(root,bg='white',fg='black',show='*',relief=SUNKEN)
e2.place(relx=0.48,rely=0.45,anchor=CENTER)

#Buttons on main window
b1 = Button(root,text='LOGIN',font=('MS Sans serif',11,'bold'),fg='navy blue',bg='white',command=get_input,relief=RAISED).place(relx=0.43,rely=0.53,anchor=CENTER)
b2 = Button(root,text='Exit',font=('verdana',11,'bold'),fg='red',bg='white',command=quitroot).place(relx=0.53,rely=0.7,anchor=CENTER)
b3 = Button(root,text='SIGN UP',font=('helventica',10,'bold'),fg='red',bg='white',command=sign_up).place(relx=0.36,rely=0.7,anchor=CENTER)
b4 = Button(root,text='Admin Login',fg='cyan',bg='blue',command=admin_login).place(relx=0.89,rely=0.36,anchor=CENTER)
Label(root,bg='white',height=7).pack(side=BOTTOM,fill=X)
root.mainloop()
