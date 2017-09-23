from Tkinter import*

def function():
    
    selection = []
    selection.append(var1.get())
    selection.append(var2.get())
    selection.append(var3.get())
    selection.append(var4.get())
    print "Initial conditions are: "
    for i in range(0,4):
      print selection[i]
    
    master.quit() 



master = Tk()
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

Label(master, text = "1. OBTAIN RELEVENT PERINATAL HISTORY").grid(row=0, sticky=W)
Label(master, text = "  A. Gestational age").grid(row=2, sticky=W)
Radiobutton(master, text = "Pre - Term", variable = var1, value = 1).grid(row=3, sticky=W)
Radiobutton(master, text = "Term", variable = var1, value = 2).grid(row=4, sticky=W)

Label(master, text = "  B. Liquor(Meconium Stained)").grid(row=5, sticky=W)
Radiobutton(master, text = "Yes", variable = var2, value = 1).grid(row=6, sticky=W)
Radiobutton(master, text = "No", variable = var2, value = 2).grid(row=7, sticky=W)

Label(master, text = "  C. Expected Number of Babies").grid(row=8, sticky=W)
Radiobutton(master, text = "Yes", variable = var3, value = 1).grid(row=9, sticky=W)
Radiobutton(master, text = "No", variable = var3, value = 2).grid(row=10, sticky=W)

Label(master, text = "  D. Associated Risk Factors").grid(row=11, sticky=W)
for i in range(len(list)):
       Radiobutton(master, text = list[i], variable = var4, value = i+1).grid(row=(i+12), sticky=W)

Label(master, text = mytext).grid(row=17, sticky=W)
Label(master, text = "3. DECIDE PLAN AND ASSIGN TEAM MEMBER ROLES").grid(row=18, sticky=W)

Button(master, text = "OK", command = function).grid(row=19, sticky=W)

mainloop()