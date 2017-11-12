from tkinter import *

root = Tk()
root.attributes('-fullscreen', True)

class allfields(object):
   i=0
   j=0
   def __init__(self,field_name):
      self.text=field_name
      self.Label=Label(root,text=self.text)
      self.entry=Entry(root)
      self.Label.grid(row=allfields.i,column=allfields.j)
      self.entry.grid(row=allfields.i,column=allfields.j+1,columnspan=2)
      allfields.i+=1

Last_name=allfields('Last Name')
First_name=allfields('First Name')
job=allfields('Job Name')
nationality=allfields('Nationality')

v=IntVar()
Label(root, width=15, text='SEX', padx=5, pady=5,anchor='w').grid(row=allfields.i+2,column=0)
Radiobutton(root,text="Male",padx = 0,variable=v, value=1).grid(row=allfields.i+2,column=1)
Radiobutton(root,text="Female",padx = 0, variable=v, value=2).grid(row=allfields.i+2,column=2)

gen_trans={1:'Male',2:'Female'}

def printer():
   var_list=[Last_name,First_name,job,nationality]
   for i in var_list:
      print (str(i.text)+":"+str(i.entry.get()))
   if int(v.get()) == 1:
      ok='Male'
   else:
      ok='Female'
   print('Sex:'+ok)
def destroy():
   root.destroy()
class Buttons(allfields):
   i=allfields.i+5
   col=1
   def __init__(self,text,fn,side):
      self.command=fn
      self.side=side
      self.text=text
      self.button=Button(root,command=self.command,text=self.text)
      self.button.grid(row=Buttons.i,column=Buttons.col)
      Buttons.col+=1

b1=Buttons('Show',printer,BOTTOM)
b2=Buttons('Quit',destroy,LEFT)


root.mainloop()
