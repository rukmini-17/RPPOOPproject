from tkinter import *
date=Tk()
date.title('date entry')
date.configure(background='white')
Label(date, text='Enter date in DD|MM|YY format: ', fg='black', bg= 'white', font=('calibri', 13)).pack(side=TOP)
Datelabel=Label(date, text=' DD: ', fg='black', bg='white', font=('calibri', 10)).place(relx=0.2, rely=0.2, anchor=CENTER)
Dateentry=Entry(date, bg= 'white', fg='black', relief=SUNKEN)
Dateentry.place(relx=0.6, rely= 0.2, anchor=CENTER)
dd=Dateentry.get()
monthlabel=Label(date, text=' MM: ', fg='black', bg='white', font=('calibri', 10)).place(relx=0.2, rely=0.4, anchor=CENTER)
monthentry=Entry(date, bg= 'white', fg='black', relief=SUNKEN)
monthentry.place(relx=0.6, rely= 0.4, anchor=CENTER)
mm=monthentry.get()
yearlabel=Label(date, text=' YY: ', fg='black', bg='white', font=('calibri', 10)).place(relx=0.2, rely=0.6, anchor=CENTER)
yearentry=Entry(date, bg= 'white', fg='black', relief=SUNKEN)
yearentry.place(relx=0.6, rely= 0.6, anchor=CENTER)
yy=yearentry.get()
#def printValue():
   # Label(date, text='{dd}, Registered!', bg='#ffbf00').pack()
dateb=Button(date,text='SAVE',font=('calibri',11),fg='white',bg='black',command=date.destroy).place(relx=0.5,rely=0.8,anchor=CENTER)
date.geometry('300x300')


print(dd, mm, yy)


date.mainloop()
