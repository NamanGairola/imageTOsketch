from tkinter import *
from itos import *
from tkinter import filedialog
from PIL import ImageTk,Image

root = Tk()
root.geometry("1000x500")
saveimg=Button(root)

def fchoosefile():
    global path
    path = filedialog.askopenfilename(initialdir="/",title="choose image",filetypes=(("jpeg files","*.jpeg"),("jpg files","*.jpg"),("png files","*.png"),("All files","*.*")))
    photo1=Image.open(path)
    rzphoto=photo1.resize((300,150),Image.ANTIALIAS)
    fphoto1=ImageTk.PhotoImage(rzphoto)
    lphoto1=Label(frame2,image=fphoto1,width=300,height=150)
    lphoto1.image=fphoto1
    lphoto1.grid(row=0,column=0,padx=5,pady=5)

def fconvert():
    sketch(path)
    global saveimg
    photo2=Image.open('chg.png')
    rzphoto=photo2.resize((300,150),Image.ANTIALIAS)
    fphoto2=ImageTk.PhotoImage(rzphoto)
    lphoto2=Label(frame2,image=fphoto2,width=300,height=150)
    lphoto2.image=fphoto2
    lphoto2.grid(row=0,column=1,padx=5,pady=5)

    saveimg.destroy()
    saveimg=Button(root,text="save",padx=50,command=fsaveimg)
    saveimg.pack(pady=10)

def fsaveimg():
    savepath=filedialog.asksaveasfilename(defaultextension=".png")
    savei(savepath)


Label1=Label(root,text="Change image to sketch",font=('',20))
frame1 = Frame(root)
choosefile = Button(frame1,text="choose\tfile",padx=50,command=fchoosefile)
convert=Button(frame1,text="convert",padx=50,command=fconvert)

frame2=Frame(root)

Label1.pack(pady=50)
frame1.pack()
choosefile.grid(row=0,column=0,padx=5)
convert.grid(row=0,column=1,padx=5)
frame2.pack()
root = mainloop()