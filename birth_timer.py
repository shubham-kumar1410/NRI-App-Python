import Tkinter as tk
import tkMessageBox
import time

root = tk.Tk()
time1 = ''

def tick():
    global time1
    time2 = time.strftime('%H:%M:%S')
    if time2 != time1:
        time1 = time2
        L2.config(text=time2)
    L2.after(200, tick)


def start():
    global birth_time
    birth_time=time.strftime('%H:%M:%S')
    B1.configure(state="disabled")
    B2.grid(row=3,column=0,pady=10,padx=10)
    B3.grid(row=4,column=0,pady=10,padx=10)
    L1.grid(row=2,column=0,pady=10)
    tick()  

def routine_care():
    tkMessageBox.showinfo("Routine Care"," 1.CUT CORD AFTER 1 MINUTE AND WITHIN 3 MINUTES \n 2.COVER BABY AND MOTHER TOGETHER \n 3.CONTINUE SKIN TO SKIN CARE \n 4.CHECK BREATHING AND COLOR \n 5.INITIATE BREASTFEEDING")

#Buttons
B1 = tk.Button(root, text="Start",command=start)
B1.grid(row=1,column=0,pady=10,padx=20)

B2 = tk.Button(root, text="YES",command=routine_care)
B2.grid_remove()

B3 = tk.Button(root, text="NO")
B3.grid_remove()

#Labels
L1= tk.Label(text="ON NEWBORN BIRTH CHECK IF \n BREATHING OR CRYING ?")
L1.grid_remove()

L2= tk.Label()
L2.grid(row=0,column=0,pady=10)


root.resizable(height=False,width=False)
root.mainloop(  )
