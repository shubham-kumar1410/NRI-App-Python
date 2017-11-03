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

Label1=Label(root,text='IF HEART RATE NOT DETECTABLE OR <60 BMP', font=('arial rounded mt', 20, 'italic'))
Label1.pack(fill=X)

blank2=Label(root,text='', font=('arial rounded mt', 10, 'italic'))
blank2.pack(fill=X)

Label2=Label(root,text='CONTINUE PPV,ADD 100% OXYGEN', font=('arial rounded mt', 20, 'italic'))
Label2.pack(fill=X)

blank3=Label(root,text='', font=('arial rounded mt', 10, 'italic'))
blank3.pack(fill=X)

Label3=Label(root,text='START CHEST COMPRESSIONS,3 COMPRESSIONS TO 1 BREATH', font=('arial rounded mt', 20, 'italic'))
Label3.pack(fill=X)

blank4=Label(root,text='', font=('arial rounded mt', 10, 'italic'))
blank4.pack(fill=X)

Label4=Label(root,text='ADMINISTER EPINEPHRINE(1:10000),0.1-0.3 ML/KG IV;IF ENDOTRACHEAL ROUTE GIVE 0.5-1.0 ML/KG', font=('arial rounded mt', 20, 'italic'))
Label4.pack(fill=X)

blank5=Label(root,text='', font=('arial rounded mt', 10, 'italic'))
blank5.pack(fill=X)

def button_countdown(i, label):
    if i > 0:
        i -= 1
        label.set(i)
        root.after(1000, lambda: button_countdown(i, label))
    else:
        close()

def close():
    root.destroy()
    import pg6

counter = 30
button_label = StringVar()
button_label.set(counter)
button_countdown(counter, button_label)


root.mainloop()
