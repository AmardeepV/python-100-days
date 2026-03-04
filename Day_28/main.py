from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #


def timer_reset():
    global reps
    window.after_cancel(timer)
    timer_label.config(text="Timer")
    check_label.config(text="")
    canvas.itemconfig(timer_text, text="00:00")
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    work_sec = WORK_MIN * 60
    short_break_Sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    reps += 1

    if reps % 8 == 0:
        timer_counterdown(long_break_sec)
        timer_label.config(text="Break", fg=RED)
        check_label.config(ext="✔")
    elif reps % 2 == 0:
        timer_counterdown(short_break_Sec)
        timer_label.config(text="Break", fg=PINK)
        check_label.config(text="✔")
    else:
        timer_counterdown(work_sec)
        timer_label.config(text="Work", fg=GREEN)
        check_label.config(text="")

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def timer_counterdown(count):
    time_in_min = math.floor(count / 60)
    time_in_sec = count % 60
    if time_in_min < 10:
        time_in_min = f"0{time_in_min}"
    if time_in_sec < 10:
        time_in_sec = f"0{time_in_sec}"

    canvas.itemconfig(timer_text, text=f"{time_in_min}:{time_in_sec}")

    if count > 0:
        global timer
        timer = window.after(1000, timer_counterdown, count - 1)
    else:
        start_timer()
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


#  Canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(103, 130, text="00:00", fill="white",
                                font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

# Timer Label
timer_label = Label(text="Timer", font=(
    FONT_NAME, 50, "bold"), fg=GREEN, bg=YELLOW)
timer_label.grid(row=0, column=1)
# Check Label
check_label = Label(fg=GREEN, bg=YELLOW)
check_label.grid(row=3, column=1)

# Start Buttons
start_button = Button(text="Start", highlightthickness=0,
                      command=start_timer)
start_button.grid(row=2, column=0)
# Reset Button
reset_button = Button(text="Reset", highlightthickness=0, command=timer_reset)
reset_button.grid(row=2, column=2)

window.mainloop()
