from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    symbols = "!#$%&()*+"
    password_list = []
    password_list += [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_list += [random.choice(symbols) for _ in range(random.randint(2,4))]
    password_list += [random.choice(numbers) for _ in range(random.randint(2,4))]
    random.shuffle(password_list)
    password = "".join(password_list)
    password_entry.delete(0,END)
    password_entry.insert(0,password)
    pyperclip.copy(password)
    return password







# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    with open("password-manager-start/data.txt","a") as data:
        website = website_entry.get()
        email = email_entry.get()
        password = password_entry.get()
        if len(website) == 0 or len(email)==0 or len(password) == 0:
            messagebox.showinfo(title="Error",message="Please do not leave any fields empty.")
        else:
            is_ok = messagebox.askokcancel(title="Confirmation",message=f"These are the details entered:\nWebsite: {website}\nEmail: {email}\nPassword: {password}\nIs it ok to save?")
            if is_ok:
                data.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0,END)
                email_entry.delete(0,END)
                password_entry.delete(0,END)
      

        






# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=20,pady=20)
canvas = Canvas(width=200,height=200)
logo_photo = PhotoImage(file="password-manager-start/logo.png")
canvas.create_image(100,100,image = logo_photo)
canvas.grid(row=0,column=1)


#Labels
website_label = Label(text= "Website:")
website_label.grid(row=1,column=0)
email_label = Label(text= "Email/Username:")
email_label.grid(row=2,column=0)
password_label = Label(text= "Password:")
password_label.grid(row=3,column=0)



#Entries
website_entry = Entry(width=55) 
website_entry.grid(row=1,column=1,columnspan=2) 
website_entry.focus()
email_entry = Entry(width=55)
email_entry.grid(row=2,column=1,columnspan=2)
email_entry.insert(0,"dredd@email.com")
password_entry = Entry(width=36)
password_entry.grid(row=3,column=1)


#Buttons
generate_password_button = Button(text="Generate Password",command=generate_password)
generate_password_button.grid(row=3,column=2)
add_button = Button(text= "Add",width=30,command=save)
add_button.grid(row=4,column=1,columnspan=2)






window.mainloop()


