import tkinter
from tkinter import*
import random
from tkinter import messagebox
from random import shuffle



answer=["club","python","wicked","darshan","coffe","jumbal","isolated","persently","steal","creeps","preserve","stream","dragged"]

words=[] 

for i in answer:
    word = list(i)
    shuffle(word)
    words.append(word)

num=random.randint(0,len(words))

def initial():
    global words,num  
    lb1.configure(text=words[num])
def ans_check():
    global words,num,answer 
    user_input=e1.get()
    if user_input==answer[num]:
        messagebox.showinfo("success","yup this is right")
        Reset()
    else:
        messagebox.showinfo("Error","nope this isn't right")
        e1.delete(0,END)
def Reset():
    global words,num,answer
    num=random.randint(0,len(words))
    lb1.configure(text=words[num])
    e1.delete(0,END)


root = tkinter.Tk()
root.geometry("300x300")

lb1 = Label(root,font='times 20')
lb1.pack(pady=30,ipady=10,ipadx=10)

answer12=StringVar()
e1=Entry(root,textvariable=answer)
e1.pack(ipady=5,ipadx=5)

Button1=Button(root,text="check",width=20,command=ans_check)
Button1.pack(pady=40)

Button2=Button(root,text="Reset",width=20,command=Reset)
Button2.pack()

initial()
root.mainloop()
