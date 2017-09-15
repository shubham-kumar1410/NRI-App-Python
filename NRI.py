from Tkinter import *
fields = 'Last Name', 'First Name', 'Job', 'Country'

def fetch(entries):
   for entry in entries:
      field = entry[0]
      text  = entry[1].get()
      print('%s: "%s"' % (field, text)) 

def makeform(root, fields):
   entries = []
   for field in fields:
      row = Frame(root)
      lab = Label(row, width=15, text=field, anchor='w')
      ent = Entry(row)
      row.pack(side=TOP, fill=X, padx=5, pady=5)
      lab.pack(side=LEFT)
      ent.pack(side=RIGHT, expand=YES, fill=X)
      entries.append((field, ent))
   v= StringVar()
   Label(root, width=15, text='SEX', padx=5, pady=5,anchor='w').pack(side=LEFT)

   Radiobutton(root,text="Male",
            padx = 0, 
            variable=v, 
            value='Male').pack(anchor = W,side=LEFT)
   Radiobutton(root, 
            text="Female",
            padx = 0, 
            variable=v, 
            value='Female').pack(anchor = W,side=LEFT)
   entries.append(('SEX',v))
   
  
   return entries
  


if __name__ == '__main__':
   root = Tk()
   root.wm_title("NRI")
   ents = makeform(root, fields)
   root.bind('<Return>', (lambda event, e=ents: fetch(e)))   
   b1 = Button(root, text='Show',
          command=(lambda e=ents: fetch(e)))
   b1.pack(side=LEFT, padx=5, pady=5)
   
   b2 = Button(root, text='Quit', command=root.quit)
   b2.pack(side=LEFT, padx=5, pady=5)
   

   root.mainloop()