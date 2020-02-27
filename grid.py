from tkinter import*

root=Tk()

myLabel1=Label(root,text='Hello Word1').grid(row=0,column=0)
myLabel2=Label(root,text='Hello Word2').grid(row=0,column=1)
myLabel3=Label(root,text='Hello Word3').grid(row=1,column=0)
myLabel4=Label(root,text='Hello Word4').grid(row=1,column=1)

root.mainloop()