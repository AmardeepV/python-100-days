from tkinter import *
from tkinter import messagebox
import random
import pyperclip

DATA_FILE = "data.txt"
LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SYMBOLS = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def gen_password():

    password_letters = []
    password_numbers = []
    password_symbols = []

    password_letters = [random.choice(LETTERS)
                        for i in range(random.randint(8, 10))]
    password_numbers = [random.choice(NUMBERS)
                        for i in range(random.randint(2, 4))]
    password_symbols = [random.choice(SYMBOLS)
                        for i in range(random.randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols
    random.shuffle(password_list)

    generated_password = "".join(password_list)
    gen_pass_entry.insert(0, string=generated_password)
    pyperclip.copy(generated_password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_data():
    website = web_entry.get()
    email = email_entry.get()
    password = gen_pass_entry.get()
    message = f"{website} | {email} | {password} \n"

    # check for empty user detail
    if len(website) == 0 or len(password) == 0 or not email.lower().endswith(".com"):
        messagebox.showerror(
            title="Error", message="one of the field is empty or the email is wrong")
    else:
        is_ok = messagebox.askokcancel(
            title=website, message=f"These are the details enterd: \n email: {email} \n password: {password} \n.Do you want to save it?")
        if is_ok:
            with open(DATA_FILE, 'a') as file:
                file.write(message)

    web_entry.delete(0, 'end')
    email_entry.delete(0, 'end')
    gen_pass_entry.delete(0, 'end')


# ---------------------------- UI SETUP ------------------------------- #
# window
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# canvas
logo_image = PhotoImage(file="logo.png")
canvas = Canvas(height=200, width=200)
canvas.create_image(100, 100, image=logo_image)
canvas.grid(row=0, column=1)

# website label
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

# email lebel
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
# password label
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# Add button
add_button = Button(text="Add", width=33, command=save_data)
add_button.grid(row=4, column=1, columnspan=2)

# Generate password button
gen_pass = Button(text="Generate Password", command=gen_password)
gen_pass.grid(row=3, column=2)

# entry
web_entry = Entry(width=35)
web_entry.focus()
web_entry.grid(row=1, column=1, columnspan=2)

# email/username entry
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)

# Generated password entry
gen_pass_entry = Entry(width=18)
gen_pass_entry.grid(row=3, column=1)


window.mainloop()
