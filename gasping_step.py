import Tkinter
import tkMessageBox

top = Tkinter.Tk()

def NoCallBack():
	#Trigger No step
	return 

def YesCallBack():
	#Next Steps (to be done)
	return

#labels
L=Tkinter.Label(top,text="INTIAL EVALUTATION \n GASPATIC/ APNEIC HR <100")
L.pack()

#buttons
B1 = Tkinter.Button(top, text ="YES EITHER OR BOTH", command = NoCallBack,padx=20,pady=20)
B1.pack()
B2 = Tkinter.Button(top, text ="NO TO BOTH", command = YesCallBack,padx=20,pady=20)
B2.pack()

if __name__ == '__main__':
	top.mainloop()