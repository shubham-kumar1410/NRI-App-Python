from Tkinter import*
import Initial_Steps
import tkMessageBox
import time




class timer:

    def __init__(self):
        self.root = Tk()
        self.time1 = ''
        #self.root.attributes('-zoomed', True)


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
        self.B1.configure(state="disabled")
        self.B2.grid(row=3,column=0,pady=10,padx=10)
        self.B3.grid(row=4,column=0,pady=10,padx=10)
        self.L1.grid(row=2,column=0,pady=10)
        self.tick()  

    def routine_care(self):
        tkMessageBox.showinfo("Routine Care"," 1.CUT CORD AFTER 1 MINUTE AND WITHIN 3 MINUTES \n 2.COVER BABY AND MOTHER TOGETHER \n 3.CONTINUE SKIN TO SKIN CARE \n 4.CHECK BREATHING AND COLOR \n 5.INITIATE BREASTFEEDING")
        self.root.quit()
        self.root.destroy()
        
        
    def NO(self):
        self.root.quit()
        self.root.destroy()
        y = Initial_Steps.Initial_Steps()
        
        y.button()
        y.label()

    #Buttons
    def button(self):
        self.B1 = Button(self.root, text="               Start               ",command=self.start,font = ("Times", 100))
        self.B1.grid(row=1,column=0,pady=10,padx=20)

        self.B2 = Button(self.root, text="YES",command=self.routine_care,font = ("Times", 35))
        self.B2.grid_remove()

        self.B3 = Button(self.root, text="NO",command = self.NO,font = ("Times", 35))
        self.B3.grid_remove()

    #Labels
    def label(self):
        self.L1= Label(text="ON NEWBORN BIRTH CHECK IF \n BREATHING OR CRYING ?",font = ("Times", 35))
        self.L1.grid_remove()

        self.L2= Label(font = ("Times",23))
        self.L2.grid(row=0,column=0,pady=10)


        self.root.resizable(height=False,width=False)
        self.root.mainloop( )