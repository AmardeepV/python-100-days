from tkinter import *
import pandas as pd
import random
import time

FILE_PATH = "data/b1_vocab.csv"
UNKNOWN_VOCAB_PATH = "data/words_to_learn.csv"
FRONT_IMAGE_PATH = "images/card_front.png"
BACK_IMAGE_PATH = "images/card_back.png"
RIGHT_IMAGE_PATH = "images/right.png"
UNKNOWN_IMAGE_PATH = "images/wrong.png"

BACKGROUND_COLOR = "#B1DDC6"

try:
    data = pd.read_csv(UNKNOWN_VOCAB_PATH)
except FileNotFoundError:
    data = pd.read_csv(FILE_PATH)
to_learn = data.to_dict(orient="records")


def pic_word():
    global current_word, flip_timer
    current_word = random.choice(to_learn)
    windows.after_cancel(flip_timer)

    canvas.itemconfig(german_title, text="German", fill="black")
    canvas.itemconfig(german_word, text=current_word['German'], fill="black")
    canvas.itemconfig(canvas_image, image=logo_image)
    flip_timer = windows.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(canvas_image, image=logo_back_image)
    canvas.itemconfig(german_title, text="English", fill="white")
    canvas.itemconfig(german_word, text=current_word['English'], fill="white")


def remove_known_word():
    print(f"Total worlds: {len(to_learn)}")
    to_learn.remove(current_word)
    df = pd.DataFrame(to_learn)
    df.to_csv(UNKNOWN_VOCAB_PATH, index=FALSE)
    pic_word()


# create the layout
windows = Tk()
windows.title("Flashy - German Language")
windows.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = windows.after(3000, func=flip_card)
# canvas
logo_image = PhotoImage(file=FRONT_IMAGE_PATH)
logo_back_image = PhotoImage(file=BACK_IMAGE_PATH)
canvas = Canvas(height=526, width=800)
canvas_image = canvas.create_image(400, 263, image=logo_image)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)

german_title = canvas.create_text(400, 150, text="Title",
                                  font=("Ariel", 40, "italic"))
german_word = canvas.create_text(
    400, 263, text="word", font=("Ariel", 60, "bold"))

canvas.grid(row=0, column=0, columnspan=2)

# # Buttons
right_button_image = PhotoImage(file=RIGHT_IMAGE_PATH)
unknown_button_iamge = PhotoImage(file=UNKNOWN_IMAGE_PATH)

right_button = Button(image=right_button_image,
                      highlightthickness=0, command=remove_known_word)
right_button.grid(row=1, column=0)
unknown_button = Button(image=unknown_button_iamge,
                        highlightthickness=0, command=pic_word)
unknown_button.grid(row=1, column=1)
pic_word()
windows.mainloop()
