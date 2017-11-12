from tkinter import*
from tkinter.messagebox import *
import birth_timer
import time


def function():
    master.destroy()
    root2=Tk()
    root2.attributes('-fullscreen', True)      
    def function2():
        root2.destroy()
        x = birth_timer.timer()
        x.button()
        x.label()
    Label(root2, text = "BIRTH\n\n",font=("Times", 25,"bold")).pack()
    Label(root2, text = "1.NOTE THE TIME OF BIRTH \n",font=("Times", 18,"bold")).pack()
    Label(root2, text = "2.RECEIVE BABY IN DRY & WARM LINEN \n",font=("Times", 18,"bold")).pack()
    Label(root2, text = "3.PLACE THE BABY PRONE ON MOTHER'S \nABDOMEN \n ",font=("Times", 18,"bold")).pack()
    Label(root2, text = "4.DRY THE BABY\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n",font=("Times", 18,"bold")).pack()
    Button(root2, text = "NEXT", fg='purple',command = function2,width=20,font = ("Times", 13)).pack(anchor='c')
    root2.mainloop()



master = Tk()
master.attributes('-fullscreen', True)
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()

def fn_info1():
    showinfo("Gestational Age-PreTerm","-Specially trained person in Preterm\n Resuscitation \n -Special attention to temperature \n management \n -CPAP and oxygen blender \ndesirable")
btn1=Button(master,text="(i)",command=fn_info1)

def fn_info2():
    showinfo("No. of expected babies:Multiple","One team per baby should be there.")
btn2=Button(master,text="(i)",command=fn_info2)

def fn_info3():
    showinfo("Associated Risk \n Factor:Antepartum Haemorrha...","Special attention should be given \n to fluid resuscitations(NS OR Rh \n Negative blood)")
btn3=Button(master,text="(i)",command=fn_info3)

list = ['Antepartum Haemorrhage', 'Diabetes', 'Hypertension' , 'Other', 'None']

Label(master, text = "Obtain Relevent Perinatal History",font=("Times", 25,"bold")).pack()
Label(master, text = "  1. Gestational age",font=("Times", 15,"bold")).pack(anchor='w')
btn1.pack(anchor='e')
Radiobutton(master, text = "Pre Term", variable = var1, value = 1,font = ("Times", 15)).pack(anchor='w')
Radiobutton(master, text = "Term", variable = var1, value = 2,font = ("Times", 15)).pack(anchor='w')

Label(master, text = "  2. Expected Number of Babies",font=("Times", 15,"bold")).pack(anchor='w')
btn2.pack(anchor='e')
Radiobutton(master, text = "Single", variable = var3, value = 1,font = ("Times", 15)).pack(anchor='w')
Radiobutton(master, text = "Plural", variable = var3, value = 2,font = ("Times", 15)).pack(anchor='w')

Label(master, text = "  3. Associated Risk Factors",font=("Times", 15,"bold")).pack(anchor='w')
btn3.pack(anchor='e')
for i in range(len(list)):
       Checkbutton(master, text = list[i], variable = var4,font = ("Times", 15)).pack(anchor='w')

Label(master,text="Perform Equipment Check Up",font = ("Times", 20,"bold")).pack(anchor='w')

Label(master, text ='a.Providing warmth',font = ("Times", 14,)).pack(anchor='w')
Label(master, text ='b.Clearing airway',font = ("Times", 14,)).pack(anchor='w')
Label(master, text ='c.Auscultation',font = ("Times", 14,)).pack(anchor='w')
Label(master, text ='d.Oxygenation',font = ("Times", 14,)).pack(anchor='w')
Label(master, text ='e.Ventilation',font = ("Times", 14,)).pack(anchor='w')
Label(master, text ='f.Incubation',font = ("Times", 14,)).pack(anchor='w')
Label(master, text ='g.Medication',font = ("Times", 14,)).pack(anchor='w')
Label(master, text = "Decide Plan And Assign Team Member Roles \n",font = ("Times", 20,"bold")).pack()

Button(master, text = "NEXT", fg='purple',command = function,width=20,font = ("Times", 13)).pack(anchor='c')

mainloop()
