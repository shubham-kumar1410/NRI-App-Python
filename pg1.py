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

Label1=Label(root,text='INITIAL STEPS', font=('arial rounded mt', 20, 'italic'))
Label1.pack(fill=X)

blank2=Label(root,text='', font=('arial rounded mt', 20, 'italic'))
blank2.pack(fill=X)

Label2=Label(root,text='INITIATE STEPS USING ROOM AIR', font=('arial rounded mt', 20, 'italic'))
Label2.pack(fill=X)

blank3=Label(root,text='', font=('arial rounded mt', 25, 'italic'))
blank3.pack(fill=X)

def destro():
    root.destroy()
    import pg2
btn=Button(root,command=destro,text='NEXT',width='10',fg='purple',height='1')
btn.pack()


root.mainloop()


#ccna exam 100-101
