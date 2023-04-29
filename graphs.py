import matplotlib as mpl 
import matplotlib.pyplot as plt    
import numpy as np  
from tkinter import *

def graph():
  lst1=["1.1.23","2.1.23","3.1.23", "4.1.23", "5.1.23"]
  lst2=[68, 70, 89, 100, 55]
  x= np.array(lst1)
  y= np.array(lst2)
  plt.title("% Students present per lecture",  fontweight='bold')
  plt.xlabel("Date")
  plt.ylabel("Percentage of students present")
  plt.plot()
  plt.bar(x, y, width= 0.4, color='lightcoral')
  plt.show()
#plt.set_facecolor("wheat")
 
date=Tk()
date.title('stats')
date.configure(background='white')
statsb=Button(date,text='Statistics',font=('calibri',12),fg='white',bg='#68B0AB',command=graph).place(relx=0.5,rely=0.8,anchor=CENTER)  #bg teal
date.geometry('300x300')
date.mainloop()