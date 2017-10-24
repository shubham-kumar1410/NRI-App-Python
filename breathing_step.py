import Tkinter
import tkMessageBox

top = Tkinter.Tk()

def NoCallBack():
	#Trigger No step
	return 

def YesCallBack():
	tkMessageBox.showinfo(" INITIAL STEPS","ENSURE OPEN AIRWAY \n CONSIDER SPO2 MONITERING \n CONSIDER CPAP(IN PRETERM); \n (if not possible start supplemental \n oxygen) and shift to NICU")
	return

#labels
L=Tkinter.Label(top,text="INTIAL EVALUTATION \n LABOURED BREATHING/ CYANOSIS")
L.pack()

#buttons
B1 = Tkinter.Button(top, text ="YES EITHER OR BOTH", command = NoCallBack,padx=20,pady=20)
B1.pack()
B2 = Tkinter.Button(top, text ="NO TO BOTH", command = YesCallBack,padx=20,pady=20)
B2.pack()

if __name__ == '__main__':
	top.mainloop()