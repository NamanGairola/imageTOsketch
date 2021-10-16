from  tkinter import *
from itos import *
from tkinter import filedialog

root = Tk()
def fchoosefile():
    root.filename = filedialog.askopenfilename(initialdir="/",title="choose image",filetypes=(("jpeg files","*.jpeg"),("jpg files","*.jpg"),("png files","*.png"),("All files","*.*")))
    sketch(root.filename)

choosefile = Button(root,text="choose\tfile",padx=50,command=fchoosefile)
choosefile.pack()
root = mainloop()