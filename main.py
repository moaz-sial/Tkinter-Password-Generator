from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import random
import pyperclip
import json
from tkinter import messagebox

# ---------------------------- FIND PASSWORD ----------------------------------- #
def find_password():
    website = website_entry.get()
    try:
        with open('data.json') as file:
            data = json.load(file)
            if website in data:
                email = data[website]['email']
                password = data[website]['password']
                messagebox.showinfo(title=website, message=f'Email: {email}\nPassword: {password}')
            else:
                messagebox.showinfo(title='Error', message='No details for the website exist.')
    except FileNotFoundError:
        messagebox.showinfo(title='Error', message='No data file found.')
    except json.JSONDecodeError:
        messagebox.showinfo(title='Error', message='Error decoding the data file.')

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_entry.delete(0, 'end')
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '<', '>', '?', '_', '-', '~', '|', '{', '}']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(4, 6)
    nr_numbers = random.randint(2, 4)

    password_letter = [random.choice(letters) for _ in range(nr_letters)]
    passowrd_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    passowrd_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letter + passowrd_symbols + passowrd_numbers
    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if website == "" or password == "" or email == "":
        messagebox.showinfo(title='Fields Empty', message="Please don't leave any field empty")
    else:
        try:
            with open('data.json', 'r') as file:
                data = json.load(file)
        except FileNotFoundError:
            with open('data.json', 'w') as file:
                json.dump(new_data, file, indent=4)
        except json.JSONDecodeError:
            with open('data.json', 'w') as file:
                json.dump(new_data, file, indent=4)
        else:
            data.update(new_data)
            with open('data.json', 'w') as file:
                json.dump(data, file, indent=4)
        finally:
            website_entry.delete(0, 'end')
            password_entry.delete(0, 'end')


window = Tk()
window.title('Password Generator')
window.config(padx=50, pady=50)

canvas = Canvas(window, width=200, height=200)
img = Image.open('C:/Users/PC/Desktop/Python Projects/Tkinter/Password Manager App/logo.png')
img = ImageTk.PhotoImage(img)
canvas.create_image(100, 100, image=img)
canvas.grid(column=1, row=0, columnspan=2)


website_label = Label(window, text="Website:")
website_label.grid(row=1, column=0, sticky="e")
email_label = Label(window, text="Email/Username:")
email_label.grid(row=2, column=0, sticky="e")
password_label = Label(window, text="Password:")
password_label.grid(row=3, column=0, sticky="e")


website_entry = Entry(window, width=35)
website_entry.grid(row=1, column=1)
website_entry.focus()
email_entry = Entry(window, width=55)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "angela@gmail.com")
password_entry = Entry(window, width=35)
password_entry.grid(row=3, column=1)


search_button = Button(window, text="Search", width=13, command=find_password)
search_button.grid(row=1, column=2)
generate_password_button = Button(window, text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)
add_button = Button(window, text="Add", width=46, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
