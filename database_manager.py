import sqlite3
mydb = sqlite3.connect("rppoop_ams.db")
cur = mydb.cursor()
#cur.execute("create database rppoop_ams")
#cur.execute("create table student_data(EnrollmentNo text(10),name text(20),password text(20))")

s = "insert into student_data(EnrollmentNo,name,password) values(?,?,?)"
b1 = ("123","omkar",'1234')
b2 = ("234","rujuta",'4523')
b3 = ("531","preet",'5423')

#dates = ['24','25','26','27','28']
#for date in dates:
'''
s = "insert into Attendance(EnrollmentNo,name,date,Physics,Chemistry,Maths) values(?,?,?,?,?,?)"
b1 = ("123","omkar",'30|04|23','P','P','P')
b2 = ("234","rujuta",'30|04|23','P','P','A')
b3 = ("345","aman",'30|04|23','A','P','P')
b4 = ("432","aditi",'30|04|23','P','P','A')
b5 = ("241","siddhi",'30|04|23','P','P','A')
b6 = ("531","preet",'30|04|23','A','P','P')
b7 = ("756","rukmini",'30|04|23','A','A','P')
b8 = ("786","akshay",'30|04|23','P','A','P')
b9 = ("432","aarya",'30|04|23','P','A','P')
cur.execute(s,b1)
cur.execute(s,b2)
cur.execute(s,b3)
cur.execute(s,b4)
cur.execute(s,b5)
cur.execute(s,b6)
cur.execute(s,b7)
cur.execute(s,b8)
cur.execute(s,b9)

s = "insert into Attendance(EnrollmentNo,name,date,Physics,Chemistry,Maths) values(?,?,?,?,?,?)"
b1 = ("123","omkar",'01|04|23','P','A','P')
b2 = ("234","rujuta",'01|04|23','P','P','A')
b3 = ("345","aman",'01|04|23','A','P','P')
b4 = ("432","aditi",'01|04|23','P','P','A')
b5 = ("241","siddhi",'01|04|23','A','P','A')
b6 = ("531","preet",'01|04|23','P','A','P')
b7 = ("756","rukmini",'01|04|23','P','P','P')
b8 = ("786","akshay",'01|04|23','A','P','P')
b9 = ("432","aarya",'01|04|23','A','A','P')
cur.execute(s,b1)
cur.execute(s,b2)
cur.execute(s,b3)
cur.execute(s,b4)
cur.execute(s,b5)
cur.execute(s,b6)
cur.execute(s,b7)
cur.execute(s,b8)
cur.execute(s,b9)

s = "insert into Attendance(EnrollmentNo,name,date,Physics,Chemistry,Maths) values(?,?,?,?,?,?)"
b1 = ("123","omkar",'02|04|23','A','P','A')
b2 = ("234","rujuta",'02|04|23','P','A','A')
b3 = ("345","aman",'02|04|23','A','P','P')
b4 = ("432","aditi",'02|04|23','P','A','A')
b5 = ("241","siddhi",'02|04|23','A','P','A')
b6 = ("531","preet",'02|04|23','P','P','P')
b7 = ("756","rukmini",'02|04|23','A','P','P')
b8 = ("786","akshay",'02|04|23','A','A','P')
b9 = ("432","aarya",'02|04|23','A','A','P')
cur.execute(s,b1)
cur.execute(s,b2)
cur.execute(s,b3)
cur.execute(s,b4)
cur.execute(s,b5)
cur.execute(s,b6)
cur.execute(s,b7)
cur.execute(s,b8)
cur.execute(s,b9)

s = "insert into Attendance(EnrollmentNo,name,date,Physics,Chemistry,Maths) values(?,?,?,?,?,?)"
b1 = ("123","omkar",'03|04|23','P','P','P')
b2 = ("234","rujuta",'03|04|23','P','A','A')
b3 = ("345","aman",'03|04|23','A','A','P')
b4 = ("432","aditi",'03|04|23','P','P','A')
b5 = ("241","siddhi",'03|04|23','A','P','A')
b6 = ("531","preet",'03|04|23','P','A','P')
b7 = ("756","rukmini",'03|04|23','A','P','P')
b8 = ("786","akshay",'03|04|23','A','P','P')
b9 = ("432","aarya",'03|04|23','P','A','A')
cur.execute(s,b1)
cur.execute(s,b2)
cur.execute(s,b3)
cur.execute(s,b4)
cur.execute(s,b5)
cur.execute(s,b6)
cur.execute(s,b7)
cur.execute(s,b8)
cur.execute(s,b9)

s = "insert into Attendance(EnrollmentNo,name,date,Physics,Chemistry,Maths) values(?,?,?,?,?,?)"
b1 = ("123","omkar",'04|04|23','A','P','P')
b2 = ("234","rujuta",'04|04|23','P','A','A')
b3 = ("345","aman",'04|04|23','P','P','P')
b4 = ("432","aditi",'04|04|23','P','P','A')
b5 = ("241","siddhi",'04|04|23','A','A','A')
b6 = ("531","preet",'04|04|23','A','A','P')
b7 = ("756","rukmini",'04|04|23','A','P','P')
b8 = ("786","akshay",'04|04|23','P','A','P')
b9 = ("432","aarya",'04|04|23','P','A','P')
cur.execute(s,b1)
cur.execute(s,b2)
cur.execute(s,b3)
cur.execute(s,b4)
cur.execute(s,b5)
cur.execute(s,b6)
cur.execute(s,b7)
cur.execute(s,b8)
cur.execute(s,b9)
'''


#cur.execute(s,b3)
#cur.execute(s,b4)
#cur.execute(s,b5)
#cur.execute(s,b6)

#cur.execute(s,b7)
#cur.execute(s,b8)
#cur.execute(s,b9)

#cur.execute(s,b10)
#cur.execute(s,b11)
#cur.execute(s,b12)


#cur.execute("create table Attendance(EnrollmentNo text(10),name text(20),Date text(20),Physics text(2),Chemistry text(2),Maths text(2))")

#cur.execute("select EnrollmentNo from student_data")
#list2 = cur.fetchall()
#list1=[item for tuple in cur.fetchall() for item in tuple]
#print(list1)
#def convertTuple(tup):
#        # initialize an empty string
#    str = ''
#    for item in tup:
#        str = str + item
#    return str

#enroll = '234'
#cur.execute("select password from student_data where EnrollmentNo = {enroll}".format(enroll='234'))
#num = cur.fetchone()
#print(num)
#list2 = [item for tuple in cur.fetchall() for item in tuple]
#print(convertTuple(num))

#cur.execute("delete from student_data where name='vardhan'")


#mydb.commit()
#cur.execute(s,b1)
#cur.execute(s,b2)
#cur.execute(s,b3)

#cur.execute("select name from student_data")
#namelist = [item for tuple in cur.fetchall() for item in tuple]
#length = len(namelist)

#cur.execute("select enrollmentNo from student_data")
#enrollList = [item for tuple in cur.fetchall() for item in tuple]
#print(namelist)
#print(enrollList)

#cur.execute("select date from Attendance")
#templist = [item for tuple in cur.fetchall() for item in tuple]
#dates = list(set(templist))
#dates.sort()
#print(dates)
'''
#cur.execute("select enrollmentNo from student_data")
#enrollList3 = [item for tuple in cur.fetchall() for item in tuple]
enrollList3 = ['rukimini','akshay','aarya']

#cur.execute("select name from student_data")
#a = [item for tuple in cur.fetchall() for item in tuple]
a = ['756','786','432']

date = '27|04|23'
entries = [['P','A','P'],['P','A','P'],['P','A','P']]


for i in range(0,len(entries)):
    s = "insert into Attendance(EnrollmentNo,name,date,Physics,Chemistry,Maths) values(?,?,?,?,?,?)"
    b1 = (enrollList3[i],a[i],date,entries[i][0],entries[i][1],entries[i][2])
    cur.execute(s,b1)
    mydb.commit()
'''

#cur.execute("delete from student_data where name = 'kumar'")
#cur.execute("delete from student_data where name = 'akshay'")
#cur.execute("delete from student_data where name = 'aarya'")
#cur.execute("delete from student_data where name = 'rukmini'")
#cur.execute("delete from attendance where date='01|05|23'")
#cur.execute("delete from attendance where date='02|05|23'")
#cur.execute("delete from attendance where date='30|04|23'")
#cur.execute("delete from attendance where date='04|05|23'")
#cur.execute("update attendance set chemistry = 'P' where enrollmentNo = '123' and date = '28|04|23'")

#cur.execute("delete from attendance")

# i am adding a line here omkar

mydb.commit()

mydb.close()
