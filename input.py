from tkinter import*

root=Tk()

e=Entry(root,width=50,bg='blue',fg='red')
e.pack()

def myClick():
	myLabel=Label(root,text=e.get(), fg='green').pack()

mybutton1=Button(root,text='Click me 1' ,command=myClick).pack()


root.mainloop()