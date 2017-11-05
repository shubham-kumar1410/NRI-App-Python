from tkinter import *
import time
root = Tk()
root.attributes('-fullscreen', True)
time1 = ''
clock = Label(root, font=('times', 40, 'bold'))
clock.pack(fill=X)
def tick():
    global time1 
    # get the current local time from the PC
    time2 = time.strftime('%H:%M:%S')
    # if time string has changed, update it
    if time2 != time1:
        time1 = time2
        clock.config(text=time2)
    # calls itself every 200 milliseconds
    # to update the time display as needed
    # could use >200 ms, but display gets jerky
    clock.after(200, tick)
tick()

blank1=Label(root,text='', font=('arial rounded mt', 10, 'italic'))
blank1.pack(fill=X)

Label1=Label(root,text='CHECK HEART RATE', font=('arial rounded mt', 20, 'italic'))
Label1.pack(fill=X)

blank2=Label(root,text='', font=('arial rounded mt', 25, 'italic'))
blank2.pack(fill=X)

def hr_60_resolve():
    root.destroy()
    import pg8
def hr_60_100_resolve():
    root.destroy()
def hr_100_resolve():
    root.destroy()
    
hr_60=Button(root,command=hr_60_resolve,text='HR<60',width='10',fg='purple',height='1')
hr_60.pack()

blank3=Label(root,text='', font=('arial rounded mt', 1, 'italic'))
blank3.pack(fill=X)

hr_60_100=Button(root,command=hr_60_100_resolve,text='HR 60-100',width='10',fg='purple',height='1')
hr_60_100.pack()

blank4=Label(root,text='', font=('arial rounded mt', 1, 'italic'))
blank4.pack(fill=X)

hr_100=Button(root,command=hr_100_resolve,text='HR>100',width='10',fg='purple',height='1')
hr_100.pack()


root.mainloop()
