from tkinter import *

window = Tk()
window.title("Mile to km converter")
window.minsize(width=400, height=50)
window.config(padx=20, pady=20)

label = Label(text="is equal to ", font=("Aerial", 20))
label.grid(row=1, column=0)

entry_miles = Entry(width=5)
entry_miles.grid(row=0, column=1)

con_label_km = Label()
con_label_km.grid(row=1, column=1)


def calculatekm():
    km = round(float(entry_miles.get()) * 1.60934, 2)
    con_label_km.config(text=str(km))


button = Button(text="Calculate", command=calculatekm)
button.grid(row=2, column=1)


label_mile = Label(text="Miles", font=("Aerial", 20))
label_mile.grid(row=0, column=2)

label_km = Label(text="Km", font=("Aerial", 20))
label_km.grid(row=1, column=2)

window.mainloop()
