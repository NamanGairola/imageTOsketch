'''
Name - Naman Gairola
Section - A
Class Roll No. - 28
University Roll No. - 2014743
Course - B.Tech CSE
'''
from tkinter import *
from itos import *
from tkinter import filedialog
from PIL import ImageTk,Image

root=Tk()
root.geometry("1000x500")
saveimg=Button(root)

# function for choosing image file
def fchoosefile():
    global path
    path=filedialog.askopenfilename(initialdir="/",title="choose image",filetypes=(("jpg files","*.jpg"),("jpeg files","*.jpeg"),("png files","*.png")))
    photo1=Image.open(path)
    rzphoto=photo1.resize((300,150),Image.ANTIALIAS)
    fphoto1=ImageTk.PhotoImage(rzphoto)
    lphoto1=Label(frame2,image=fphoto1,width=300,height=150)
    lphoto1.image=fphoto1
    lphoto1.grid(row=0,column=0,padx=5,pady=5)

# function to convert image to sketch and making save button appear
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

# function for saving converted image
def fsaveimg():
    savepath=filedialog.asksaveasfilename(defaultextension=".png")
    savei(savepath)

#background image
bgi=ImageTk.PhotoImage(file="bg.jpg")
bglabel=Label(root,image=bgi)

# labels and buttons
Label1=Label(root,text="Convert Image To Sketch",font=('Times',30,"bold"),bg="#ffff00")
restrict=Label(root,text="Ensure your image if of format .jpg/.jpeg/.png/ and size do not exceed 20MB",font=('',10),bg="#ffff00",fg='red')
frame1=Frame(root,bg="#ffff00")
choosefile=Button(frame1,text="choose\tfile",padx=50,command=fchoosefile)
convert=Button(frame1,text="convert",padx=50,command=fconvert)

frame2=Frame(root,bg="#ffff00")
#putting label and frame on screen
bglabel.place(x=0,y=0)
Label1.pack(pady=(60,5))
restrict.pack(pady=10)
frame1.pack()
choosefile.grid(row=0,column=0,padx=5)
convert.grid(row=0,column=1,padx=5)
frame2.pack()
root.mainloop()