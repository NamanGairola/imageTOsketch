from tkinter import *
from itos import *
from tkinter import filedialog

root = Tk()
root.geometry("500x250")
saveimg=Button(root)

def fchoosefile():
    global path
    path = filedialog.askopenfilename(initialdir="/",title="choose image",filetypes=(("jpeg files","*.jpeg"),("jpg files","*.jpg"),("png files","*.png"),("All files","*.*")))

def fconvert():
    sketch(path)
    global saveimg
    saveimg.destroy()
    saveimg=Button(root,text="save",padx=50,command=fsaveimg)
    saveimg.pack(pady=10)

def fsaveimg():
    savepath=filedialog.asksaveasfilename(defaultextension=".jpg")
    savei(savepath)

Label1=Label(root,text="Change image to sketch",font=('',20))
frame1 = Frame(root)
choosefile = Button(frame1,text="choose\tfile",padx=50,command=fchoosefile)
convert=Button(frame1,text="convert",padx=50,command=fconvert)
Label1.pack(pady=50)
frame1.pack()
choosefile.grid(row=0,column=0,padx=5)
convert.grid(row=0,column=1,padx=5)
root = mainloop()