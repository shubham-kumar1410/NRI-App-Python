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

Label1=Label(root,text='ENSURE OPEN AIRWAY', font=('arial rounded mt', 20, 'italic'))
Label1.pack(fill=X)

blank2=Label(root,text='', font=('arial rounded mt', 35, 'italic'))
blank2.pack(fill=X)

def yespart():
    root.destroy()
    import pg6
yes_button=Button(root,command=yespart,text='NEXT',width='10',fg='purple',height='1')
yes_button.pack()


root.mainloop()
