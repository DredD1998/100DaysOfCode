from tkinter import *


window = Tk()
window.title("My First GUI Program")
window.minsize(500, 300)
window.config(padx=20,pady=20)

my_label = Label(text="I am a Label",font=("Arial",12,"bold"))



my_label["text"] = "New Text"
my_label.grid(column=0,row=0)




def button_clicked():
    print("I got clicked!")
    new_text = input.get()
    my_label["text"] = new_text

button = Button(text= "Click Me!",command=button_clicked)
button.grid(column=2,row=2)

new_button = Button(text="New Button!")
new_button.grid(column=3,row=3)

input = Entry(width=20)
input.grid(column=1,row=1)

print(input.get())



window.mainloop() 