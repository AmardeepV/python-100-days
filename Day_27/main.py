from tkinter import *

window = Tk()
window.title("My first gui program")
window.minsize(width=500, height=300)

# label
label = Label(text="I am a label", font=("Aerial", 24))
label.grid(row=0, column=0)


def button_click():
    input_data = input.get()
    label['text'] = input_data


# button
button_one = Button(text="Click here", command=button_click)
button_one.grid(row=1, column=1)

button_two = Button(text="click me", command=button_click)
button_two.grid(row=0, column=2)

# Entry
input = Entry(width=20)
input.grid(row=2, column=3)


window.mainloop()
