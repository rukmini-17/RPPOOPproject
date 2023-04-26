#DIGITAL ATTENDANCE MANAGEMENT SYSTEM     

from tkinter import*
import sqlite3
from decimal import Decimal
#from PIL import ImageTk, Image

'''
READ ME: ABOUT DATABASES
1. STUDENT DATA
2. ATTENDANCE
'''

def convertTuple(tup):
    str = ''
    for item in tup:
        str = str + item
    return str


#SQL CONNECTION (DONE BY OMKAR)
mydb = sqlite3.connect("rppoop_ams.db")
cur = mydb.cursor()


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


#For LOGIN BUTTON (SQL upgrade done!)
def get_input():

    enrollmentNo = e1.get()   #e1 = enrollment entry box
    password = e2.get()       #e2 = password entry box

    #get contents of EnrollmentNo::student data into enrollList
    cur.execute("select EnrollmentNo from student_data")
    enrollList = [item for tuple in cur.fetchall() for item in tuple]   

    cur.execute("select name from student_data where EnrollmentNo = {var}".format(var = enrollmentNo))
    name = convertTuple(cur.fetchone()) 

    if enrollmentNo!='' and password!='':     
        
        #correct enrollmentNo condition
        if enrollmentNo in enrollList:

            cur.execute("select password from student_data where EnrollmentNo = {var}".format(var = enrollmentNo))
            pwd = convertTuple(cur.fetchone())
            
            #correct password condition
            if password == pwd:
                e1.delete(0,END)
                e2.delete(0,END)
                profile=Tk()
                profile.configure(background='white')
                profile.title('Student Profile')
                l=Label(profile,text='WELCOME '+ name.upper() + ' !',fg='blue',bg='white',font=('Times New Roman',8,'bold')).grid(row=0,column=2)
                
                #get date data
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
                pa = [item for tuple in cur.fetchall() for item in tuple]   #physics attendance
                
                for j2 in range(0,k):
                    list_P.insert(j2+1,pa[j2])
                    if pa[j2] =='P':
                        list_P.itemconfig(j2+1,{'fg':'green'})
                    elif pa[j2] =='A':
                        list_P.itemconfig(j2+1,{'fg':'red'})
                
                #chemistry attendance output
                cur.execute("select Chemistry from Attendance")
                ca = [item for tuple in cur.fetchall() for item in tuple]   #chemistry attendance
 
                for j3 in range(0,k):
                    list_C.insert(j3+1,ca[j3])
                    if ca[j3]=='P':
                        list_C.itemconfig(j3+1,{'fg':'green'})
                    elif ca[j3]=='A':
                        list_C.itemconfig(j3+1,{'fg':'red'})
                
                #maths attendance output
                cur.execute("select Maths from Attendance")
                ma = [item for tuple in cur.fetchall() for item in tuple]   #maths attendance
  
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
                
                atdPt=Decimal((int(p1)/(int(p1)+int(a1)))*100)
                atdCt=Decimal((int(p2)/(int(p2)+int(a2)))*100)
                atdMt=Decimal((int(p3)/(int(p3)+int(a3)))*100)
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
            
            #Wrong password condition
            elif enrollmentNo in enrollList and password != pwd:
                e2.delete(0,END)
                wrong=Tk()
                wrong.configure(background='white')
                l=Label(wrong,text='WRONG PASSWORD ENTERED!!!\nENTER PASSWORD AGAIN.',fg='red',bg='white',font='times,5').pack()
                k=Button(wrong,text='Okay',fg='blue',bg='white',command=wrong.destroy).pack()
                wrong.mainloop()
        
        #Wrong EnrollmentNo condition
        else:
            e1.delete(0,END)
            e2.delete(0,END)
            r=Tk()
            r.configure(background='white')
            Label(r,text='INVALID ENROL NO. OR PASSWORD !',fg='red',bg='white').pack()
            Button(r,text='Okay',bg='white',command=r.destroy).pack()
            r.mainloop()
    else:
        r=Tk()
        r.configure(background='white')
        Label(r,text='ENTER DATA!',fg='red',bg='white').pack(fill=X)
        Button(r,text='Okay',fg='blue',bg='white',command=r.destroy).pack(fill=X)
        r.mainloop()
            
            
b1=Button(root,text='LOGIN',font=('MS Sans serif',11,'bold'),fg='navy blue',bg='white',command=get_input,relief=RAISED).place(relx=0.43,rely=0.53,anchor=CENTER)

#FOR EXIT BUTTON (No changes required)
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
    
b2=Button(root,text='Exit',font=('verdana',11,'bold'),fg='red',bg='white',command=quitroot).place(relx=0.53,rely=0.7,anchor=CENTER)

#FOR SIGNUP BUTTON  (SQL upgrade done!)
def new_entry():
    new=Tk() 
    new.configure(background='white')
    new.title('NEW ENTRY')  #create new entry window with name, mis, pwd, confirm pwd labels and entries
    l1=Label(new,text=' NAME :',fg='blue',bg='white',font=('Times New Roman',10)).place(relx=0.3,rely=0.2,anchor=CENTER)
    n1=Entry(new)
    n1.place(relx=0.6,rely=0.2,anchor=CENTER)
    l2=Label(new,text='ENROLMENT NO :',fg='blue',bg='white',font=('Times New Roman',10)).place(relx=0.25,rely=0.37,anchor=CENTER) 
    n2=Entry(new)
    n2.place(relx=0.6,rely=0.37,anchor=CENTER)
    l3=Label(new,text='        PASSWORD :',fg='blue',bg='white',font=('Times New Roman',10)).place(relx=0.25,rely=0.55,anchor=CENTER)
    n3=Entry(new,show='*')
    n3.place(relx=0.6,rely=0.55,anchor=CENTER)
    l4=Label(new,text='CONFIRM PASSWORD :',fg='blue',bg='white',font=('Times New Roman',10)).place(relx=0.220,rely=0.7,anchor=CENTER)
    n4=Entry(new,show='*')
    n4.place(relx=0.6,rely=0.7,anchor=CENTER)
    new.geometry('400x400') #size of new

    def n_save():
        cur.execute("select EnrollmentNo from student_data")
        list1=[item for tuple in cur.fetchall() for item in tuple]   #get contents of EnrollmentNo::student data into list1
          
        if n1.get()=='' or n2.get()=='' or n3.get()=='' or n4.get()=='': #if all fields are not filled ask user to fill them
            v=Tk()
            v.configure(background='white')
            n=Label(v,text='ENTER DATA!',fg='red',bg='white',font='times,4').pack()
            d=Button(v,text='OKAY',fg='blue',bg='white',command=v.destroy).pack()
            v.mainloop()
        
        elif any((n1.get()) in s for s in list1): #if the entry already exists don't make a new one ie delete the new one 
            def re_data():
                q.destroy()
                n1.delete(0,END)
                n2.delete(0,END)
                n3.delete(0,END)
                n4.delete(0,END)
            q=Tk()
            q.configure(background='white')
            l=Label(q,text='Data Already Exists!',fg='red',font='times,6').pack()
            but=Button(q,text='Okay',fg='blue',bg='white',command=re_data).pack()
            q.mainloop()
        
        else: 
            s = "insert into student_data(EnrollmentNo,name,password) values(?,?,?)"
            b1 = (n2.get(),n1.get(),n3.get())
            cur.execute(s,b1)
            mydb.commit()
            n1.delete(0,END) 
            n2.delete(0,END)
            n3.delete(0,END)
            n4.delete(0,END)
            q=Tk()
            q.configure(background='white')
            L=Label(q,text='Entry Saved',fg='green',bg='white',font='helventica,5').pack()
            B=Button(q,text='Okay',fg='blue',bg='white',font='times,3',command=q.destroy).pack()
            q.mainloop()
                                 
    b1=Button(new,text='SAVE',command=n_save,fg='red',bg='white',font=('Helventica',8)).place(relx=0.5,rely=0.85,anchor=CENTER)        
    new.mainloop() #now the new entry is saved  

            
#FOR ADMIN LOGIN
def am():
    def td():
        if k.get()=='admin':   #k is the admin password
            ad.destroy()
            a=Tk()
            a.configure(background='white')
            a.title('ADMIN')
            Label(a,text='CHOOSE LECTURE :',fg='purple',bg='white',font=('Times New Roman',25)).pack(fill=X)
            
            def phy_atd():
                
                check = '28|04|23'   #NOTE: GENERATE A WINDOW TO ACCEPT DATE (RUKMINI??)

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
                              
            b1=Button(a,text='PHYSICS',fg='orange',bg='white',font=('Verdana',16,'bold'),height=5,width=8,command=phy_atd)
            b1.pack(fill=X)

            
            def chem_atd():
                check = '28|04|23'   #NOTE: GENERATE A WINDOW TO ACCEPT DATE (RUKMINI??)
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

            b2=Button(a,text='CHEMISRY',fg='orange',bg='white',font=('Verdana',16,'bold'),height=5,width=8,command=chem_atd)
            b2.pack(fill=X)

            
            def mat_atd():
                check = '28|04|23'   #NOTE: GENERATE A WINDOW TO ACCEPT DATE (RUKMINI??)
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

            b3=Button(a,text='MATHS',fg='orange',bg='white',font=('Verdana',16,'bold'),height=5,width=8,command=mat_atd)
            b3.pack(fill=X)

            #SQL upgrade done!
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
                    a.destroy()
                Button(see,text='LOG OUT',fg='blue',bg='white',font=('Helventica',10,'bold'),command=logout).grid(row=6,column=1)
                Button(see,text='CLOSE',fg='red',bg='white',font=('Helventica',10,'bold'),command=see.destroy).grid(row=6,column=0)
                Label(see,text='N = NOT AVAILABLE',fg='red').grid(row=6,column=2)
                see.mainloop()
                    
            b4=Button(a,text='SEE ATTENDANCE',fg='blue',bg='white',font=('times',16,'bold'),height=5,width=8,command=see_atd)
            b4.pack(fill=X)
            a.mainloop()
        else:
            k.delete(0,END)
            d=Tk()
            d.configure(background='white')
            Label(d,text='Wrong Password!',fg='red',bg='white',font=('Times',12,'bold')).pack(fill=X)
            Button(d,text='Okay',bg='white',command=d.destroy).pack(fill=X)
             
    ad=Tk()
    ad.configure(background='white')
    Label(ad,text='ENTER PASSWORD :',fg='purple',bg='white',font=('Times New Roman',13,'bold italic')).pack()
    k=Entry(ad,show='*',fg='magenta')
    k.pack()
    Button(ad,text='LOGIN',fg='blue',bg='white',command=td).pack()
    ad.mainloop()
    
b3=Button(root,text='SIGN UP',font=('helventica',10,'bold'),fg='red',bg='white',command=new_entry).place(relx=0.36,rely=0.7,anchor=CENTER)
Button(root,text='Admin Login',fg='cyan',bg='blue',command=am).place(relx=0.89,rely=0.36,anchor=CENTER)
Label(root,bg='white',height=7).pack(side=BOTTOM,fill=X)
root.mainloop()
