
from tkinter import* 


top=Tk()
top.title("E-commerce")
count=0
count1=0

def addrec():

    f=open('dbs.txt','a')

    ItemName=s1.get()

    ItemNo=s2.get()

    Price=s3.get()

    MfgDate=s4.get()

    ExpDate=s5.get()

    f.writelines(ItemNo.ljust(20)+ItemNo.ljust(10)+Price.ljust(30)+ MfgDate.ljust(15)+ExpDate.ljust(15)+"\n")
    global count
    global count1

    f.close()
    s1.set("")
    s2.set("")
    s3.set("")
    s4.set("")
    s5.set("")

def nextrec():

    i=0

    f=open('dbs.txt','r')

    global count

    while(i<=count):

        l=f.readline()

        i=i+1

    l1=l.split()

    # print(l1[0],l1[1])	# If we want to print on console screen

    s1.set(l1[0])	

    s2.set(l1[1])

    s3.set(l1[2])

    s4.set(l1[3])

    s5.set(l1[4])

    count=count+1

    f.close()


def prev():

    f=open('dbs.txt','r')

    i=0

    global count

    count=count-1

    while(i<=count-1):

        i=i+1


    l=f.readline(i-1)

        

    l5=l.split()

    # print(l1[0],l1[1])	# If we want to print on console screen

    s1.set(l5[0])	

    s2.set(l5[1])

    s3.set(l5[2])

    s4.set(l5[3])

    s5.set(l5[4])

    

    f.close()  

def delete():

    k=[s1.get(), s2.get(), s3.get(), s4.get(), s5.get()]

    f=open('dbs.txt',"r")

    h=f.readlines()

    f.close()

    f=open('dbs.txt',"w")

    for i in h:

        j=i.split()

        if(j!=k):

            f.writelines(j[0].ljust(20)+j[1].ljust(10)+j[2].ljust(30)+j[3].ljust(15)+j[4].ljust(15)+"\n")

    f.close()


def search():
  try:

    k=s1.get()

    f=open('dbs.txt',"r")

    h=f.readlines()

    for i in h:

        j=i.split()

        if(j[0]==k):

            s1.set(j[0])

            s2.set(j[1])

            s3.set(j[2])

            s4.set(j[3])

            s5.set(j[4])
  except:
    print( 'no such entry')  
    f.close()
   
        
   
def update():
  try:

    ItemName=s1.get()

    ItemNo=s2.get()

    Price=s3.get()

    MgfDate=s4.get()

    ExpDate=s5.get()

    f=open("dbs.txt","r")

    h=f.readlines()
  except:

    print('no entry for updation')
 
    f.close()

    f=open("dbs.txt","w")

    flag=0

    for i in h:

        j=i.split()

        if(j[0]!=brand):

            f.writelines(j[0].ljust(20)+j[1].ljust(10)+j[2].ljust(30)+j[3].ljust(15)+j[4].ljust(15)+"\n")

        else :

            f.writelines(ItemName.ljust(20)+ItemNo.ljust(10)+Price.ljust(30)+MfgDate.ljust(15)+ExpDate.ljust(15)+"\n")

            flag=1

    f.close()



def lr():
  try:

    f=open('dbs.txt','r')

    a=0

    b=0

    for i in f:

        a=a+1

    f.seek(0)

    h=f.readlines()

    l=list(h)

    l1=l[a-1].split()

    s1.set(l1[0])	

    s2.set(l1[1])

    s3.set(l1[2])

    s4.set(l1[3])

    s5.set(l1[4])
  
  except:

    print('no such record')
    f.close()


def fr():

    f=open('dbs.txt','r')

    a=0

    b=0

    for i in f:

        a=a+1

    f.seek(0)

    h=f.readlines()

    l=list(h)

    l1=l[0].split()

    s1.set(l1[0])	

    s2.set(l1[1])

    s3.set(l1[2])

    s4.set(l1[3])

    s5.set(l1[4])

    f.close()

s1=StringVar()

s2=StringVar()

s3=StringVar()

s4=StringVar()

s5=StringVar()


          
 





l1=Label(top,text="ItemName")
l2=Label(top,text="ItemNo")
l3=Label(top,text ="Price")
l4=Label(top,text="MfgDate")
l5=Label(top,text="ExpDate")
t1=Entry(top,textvariable=s1)

t2=Entry(top,textvariable=s2)

t3=Entry(top,textvariable=s3)

t4=Entry(top,textvariable=s4)

t5=Entry(top,textvariable=s5)
b1=Button(top,text="Next", command=nextrec)

b2=Button(top,text="Add", command=addrec)

b3=Button(top,text="Delete", command=delete)

b4=Button(top,text="Search", command=search)

b5=Button(top,text="Update", command=update)

b7=Button(top,text="Last Record", command=lr)

b6=Button(top,text="First Record", command=fr)

b8=Button(top,text="Previous", command=prev)




l1.grid(row=2,column=1)

l2.grid(row=3,column=1)

l3.grid(row=4,column=1)

l4.grid(row=5,column=1)

l5.grid(row=6,column=1)

t1.grid(row=2,column=2)

t2.grid(row=3,column=2)

t3.grid(row=4,column=2)

t4.grid(row=5,column=2)

t5.grid(row=6,column=2)

b1.grid(row=12,column=2)

b2.grid(row=11,column=1)

b3.grid(row=11,column=2)

b4.grid(row=8,column=4)

b5.grid(row=11,column=4)

b6.grid(row=8,column=1)

b7.grid(row=8,column=2)

b8.grid(row=12,column=1)




top.mainloop()
    

    

