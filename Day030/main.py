
import json
from tkinter import *
import random
from tkinter import messagebox
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for letter in range(nr_letters)]
    password_symbols = [random.choice(symbols) for symbol in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for number in range(nr_numbers)]

    password_list=password_letters+password_numbers+password_symbols

    random.shuffle(password_list)

    password= "".join(password_list)

    password_entry.insert(0,password)
    pyperclip.copy(password)

# ---------------------------- SEARCH ------------------------------- #



# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website=website_entry.get()
    email=email_entry.get()
    password=password_entry.get()
    new_data ={
        website: {
            "Email" : email,
            "Password": password
        }
    }

    if website == 0 or password ==0:
        messagebox.showinfo(title="Oops" , message="Please make sure you haven't left any field empty")

    else:
        try:
            with open("data.json","r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json","w") as data_file:
                json.dump(new_data,data_file,indent=4)
        else:
                data.update(new_data)
                with open("data.json","w") as data_file:
                    json.dump(data,data_file,indent=4)
        finally:
                website_entry.delete(0,END)
                password_entry.delete(0,END)

def search_password():
    website=website_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
            messagebox.showinfo(title="Error",message="No data file found")
    else:
            if website in data:
                email = data[website]["Email"]
                password= data[website]["Password"]
                messagebox.showinfo(title=website,message=f"Email: {email}\nPassword: {password}")
            else:
                messagebox.showinfo(title="Error",message=f"No details for {website} exists")

# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

canvas=Canvas(height=200,width=200)
image=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=image)
canvas.grid(row=0,column=1)


website_label=Label(text="Website")
website_label.grid(row=1,column=0)
email_label=Label(text="Email")
email_label.grid(row=2,column=0)
password_label= Label(text="Password")
password_label.grid(row=3,column=0)

website_entry=Entry(width=35)
website_entry.grid(row=1,column=1,columnspan=2)
website_entry.focus()

email_entry=Entry(width=35)
email_entry.grid(row=2,column=1,columnspan=2)
email_entry.insert(0,"hajrarafiq1828@gmail.com")

password_entry=Entry(width=35)
password_entry.grid(row=3,column=1,columnspan=2)

generate_password_button=Button(text="Generate", width=8 ,command=generate_password)
generate_password_button.grid(row=3,column=2)
search_button=Button(text="Search", width=8 ,command=search_password)
search_button.grid(row=1,column=2)
add_button=Button(text="Add",width=33,command=save)
add_button.grid(row=4,column=1,columnspan=2)

search_password()


window.mainloop()