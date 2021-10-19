from  tkinter import *
from itos import *
from tkinter import filedialog

root = Tk()
def fchoosefile():
    global path
    path = filedialog.askopenfilename(initialdir="/",title="choose image",filetypes=(("jpeg files","*.jpeg"),("jpg files","*.jpg"),("png files","*.png"),("All files","*.*")))

def fconvert():
    sketch(path)

Label1=Label(root,text="Change image to sketch")
choosefile = Button(root,text="choose\tfile",padx=50,command=fchoosefile)
convert=Button(root,text="convert",padx=50,command=fconvert)
Label1.grid(row=0,column=0)
choosefile.grid(row=1,column=0)
convert.grid(row=1,column=1)
root = mainloop()