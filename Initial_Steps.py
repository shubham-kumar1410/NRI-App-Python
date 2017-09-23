from Tkinter import*
import tkMessageBox
import time

mytext = "INITIAL STEPS \n -Clamp and cut cord immediately \n -Place under radiant warmer \n -Postition head with neck slightly extended \n -Clear airway by suctioning mouth then nose \n Stimulate by running the back \n Reposition"


class Initial_Steps:

	def __init__(self):
		self.root = Tk()
		self.time1 = ''
		self.root.attributes('-zoomed', True)

	def tick(self):
		global time1
		self.time2 = time.strftime('%H:%M:%S')
		if self.time2 != self.time1:
		    self.time1 = self.time2
		    self.L2.config(text=self.time2)
		self.L2.after(200, self.tick)

	def start(self):
		global birth_time
		birth_time=time.strftime('%H:%M:%S')
		self.tick()

	def button(self):
		self.B3 = Button(self.root, text="                     NEXT                          ",font = ("Times", 70)).grid(row=40, sticky=W)
		
	#Labels
	def label(self):

		self.L1= Label(text=mytext,font = ("Times", 42))
		#self.L3 = Label(text="Initial Steps: ",font = ("Times", 40,"bold").grid(row = 4,sticky = W)
		self.L1.grid(row=20,column=0,pady=10)
		#self.L1.grid_remove()
		self.L2 = Label(font = ("Times",23))
		self.L2.grid(row=0,column=0,pady=10)
		self.start()

		self.root.resizable(height=False,width=False)
		self.root.mainloop( )