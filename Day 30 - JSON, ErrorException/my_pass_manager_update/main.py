from tkinter import *
from tkinter import messagebox
import json

import subprocess
subprocess.run(["pip", "install", "pyperclip"])
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
from random import randint,choice,shuffle

def generate_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters=[choice(letters) for _ in range(randint(8,10))]
    password_numbers=[choice(numbers) for _ in range(randint(2,4))]
    password_symbols=[choice(symbols) for _ in range(randint(2,4))]
    
    password_list=password_letters+password_numbers+password_symbols
    shuffle(password_list)
    
    pass_entry.delete(0,END)
    pass_entry.insert(0,"".join(password_list))
    pyperclip.copy("".join(password_list))

# ---------------------------- SAVE / LOAD PASSWORD ------------------------------- #
def save(event=None):
    if(website_entry.get()=="" and email_data.get()=="" and pass_data.get()==""):
        messagebox.showwarning(title="Nuhuh",message="Dont leave empty fields >:|")
    else:
        website_data=website_entry.get().strip()
        email_data=email_entry.get().strip()
        pass_data=pass_entry.get().strip()
        finalized_data={
            website_data:{
                "email": email_data,
                "password": pass_data,
            }
        }
        
        # prompt=messagebox.askokcancel(title=website_data,message=f"These are the details entered: \nEmail: {email_data} "
        #                        f"\nPassword: {pass_data} \nIs it ok to save?")
        
        #if(prompt):
        
        try:
            with open("data.json","r") as data_file:
                updated_data=json.load(data_file)
                updated_data.update(finalized_data)
        except FileNotFoundError:
            updated_data=finalized_data
        finally:
            with open("data.json","w") as data_file:
                json.dump(updated_data, data_file,indent=4)
                
                website_entry.delete(0,END)
                pass_entry.delete(0,END)

def find_password(event=None):
    website=website_entry.get()
    try:
        with open("data.json","r") as data_file:
            data=json.load(data_file)
    except FileNotFoundError:
        messagebox.showwarning(title="Error",message="data.json not found!")
    else:
        if website in data:
            try:
                email=data[website]["email"]
                password=data[website]["password"]
            except KeyError:
                messagebox.showwarning("Data for this website not found or incorrect!")
            else:
                messagebox.showinfo(title=website,message=f"Email: {email}\nPassword: {password}")
                pyperclip.copy("".join(password))
        else:
            messagebox.showwarning(title="Error",message=f"No details for {website} exists.")
# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("MyPass Manager")
window.config(padx=50,pady=50)

CANVAS_WIDTH=200
CANVAS_HEIGHT=200
canvas=Canvas(width=CANVAS_WIDTH,height=CANVAS_HEIGHT)
logo_img=PhotoImage(file="logo.png")
canvas.create_image(CANVAS_WIDTH/2,CANVAS_HEIGHT/2,image=logo_img)
canvas.grid(row=0,column=1)


website_label=Label(text="Website: ")
website_label.grid(row=1,column=0)

website_entry = Entry()
website_entry.grid(row=1,column=1, sticky="EW")
website_entry.focus()

seatch_button = Button(text="Search")
seatch_button.grid(row=1,column=2, sticky="EW")
seatch_button["command"]=find_password


email_label=Label(text="Email/Username: ")
email_label.grid(row=2,column=0)

email_entry = Entry()
email_entry.grid(row=2,column=1,columnspan=2, sticky="EW")
try:
    with open("default_email.txt") as def_email_file:
        email_entry.insert(0,def_email_file.read())
except:
    email_entry.insert(0,"test@gmail.com")


pass_label=Label(text="Password: ")
pass_label.grid(row=3,column=0)

pass_entry = Entry()
pass_entry.grid(row=3,column=1, sticky="EW")

pass_button = Button(text="Generate Password")
pass_button.grid(row=3,column=2, sticky="EW")
pass_button["command"]=generate_pass


add_button = Button(text="Add",width=35)
add_button.grid(row=4,column=1,columnspan=2, sticky="EW")
add_button["command"]=save
window.bind('<Return>', save)

window.mainloop()