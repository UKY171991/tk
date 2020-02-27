from tkinter import*

root=Tk()

mybutton1=Button(root,text='Click me 1').grid(row=0,column=0)
mybutton2=Button(root,text='Click me 2').grid(row=0,column=1)
mybutton3=Button(root,text='Click me 3').grid(row=1,column=0)
mybutton4=Button(root,text='Click me 4').grid(row=1,column=1)

root.mainloop()