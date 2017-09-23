from Tkinter import*
import tkMessageBox
import birth_timer
import time


def function():
    tkMessageBox.showinfo("Routine Care"," 1.NOTE THE TIME OF BIRTH \n 2.RECEIVE BABY IN DRY & WARM LINEN \n 3.PLACE THE BABY PRONE ON MOTHER'S ABDOMEN \n 4.DRY THE BABY")
    master.quit() 
    master.destroy()
    x = birth_timer.timer()
    x.button()
    x.label()



master = Tk()
master.attributes('-zoomed', True)
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()

list = ['Antepartum Haemorrhage', 'Diabetes', 'Hypertension' , 'Other', 'None']
mytext = """2. PERFORM EQUIPMENT CHECK UP
          a. Providing warmth
      b. Clearing airway
   c. Auscultation
   d. Oxygenation
e. Ventilation
f. Intubation
g. Medication
"""

Label(master, text = "1. OBTAIN RELEVENT PERINATAL HISTORY",font=("Times", 17,"bold")).grid(row=0, sticky=W)
Label(master, text = "  A. Gestational age",font=("Times", 15,"bold")).grid(row=2, sticky=W)
Radiobutton(master, text = "Pre - Term", variable = var1, value = 1,font = ("Times", 15)).grid(row=3, sticky=W)
Radiobutton(master, text = "Term", variable = var1, value = 2,font = ("Times", 15)).grid(row=4, sticky=W)

Label(master, text = "  B. Liquor(Meconium Stained)",font=("Times", 15,"bold")).grid(row=5, sticky=W)
Radiobutton(master, text = "Yes", variable = var2, value = 1,font = ("Times", 15)).grid(row=6, sticky=W)
Radiobutton(master, text = "No", variable = var2, value = 2,font = ("Times", 15)).grid(row=7, sticky=W)

Label(master, text = "  C. Expected Number of Babies",font=("Times", 15,"bold")).grid(row=8, sticky=W)
Radiobutton(master, text = "Single", variable = var3, value = 1,font = ("Times", 15)).grid(row=9, sticky=W)
Radiobutton(master, text = "Plural", variable = var3, value = 2,font = ("Times", 15)).grid(row=10, sticky=W)

Label(master, text = "  D. Associated Risk Factors",font=("Times", 15,"bold")).grid(row=11, sticky=W)
for i in range(len(list)):
       Radiobutton(master, text = list[i], variable = var4, value = i+1,font = ("Times", 15)).grid(row=(i+12), sticky=W)

Label(master, text = mytext,font = ("Times", 12,)).grid(row=17, sticky=W)
Label(master, text = "3. DECIDE PLAN AND ASSIGN TEAM MEMBER ROLES",font = ("Times", 12)).grid(row=18, sticky=W)

Button(master, text = "OK", command = function).grid(row=19, sticky=W)

mainloop()