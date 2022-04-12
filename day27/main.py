from tkinter import *

window = Tk()
window.title("My GUI Program")
window.minsize(500,300)
window.configure(bg="#FFFBE7")

my_label = Label(text="Hello World!",font=("Arial",20,"italic"))
my_label.grid(row=0,column=0)

def button_click():
    my_label.config(text="New")
    my_label.config(text=input.get())



button = Button(text="Click Here", command=button_click)
button.grid(row=2,column=2)

button2=Button(text="Hi i am here")
button2.grid(row=0,column=4)

input = Entry(width=10,bg = "#eee")
input.grid(row=4,column=6)
input.get()

window.mainloop()