from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface():
    def __init__(self, quiz: QuizBrain):

        self.quiz = quiz
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # buttons
        self.right_image = PhotoImage(file="images/true.png")
        self.wrong_image = PhotoImage(file="images/false.png")

        self.right_button = Button(
            image=self.right_image, highlightthickness=0, command=self.check_right_button)
        self.right_button.grid(row=2, column=0)

        self.wrong_button = Button(
            image=self.wrong_image, highlightthickness=0, command=self.check_wrong_button)
        self.wrong_button.grid(row=2, column=1)

        # label
        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        # canvas
        self.question_canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.question_canvas.create_text(150,
                                                              125,
                                                              width=280,
                                                              text="some question to ask ",
                                                              fill=THEME_COLOR,
                                                              font=("Arial", 20, "italic"))
        self.question_canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.canvas_question()
        self.window.mainloop()

    def canvas_question(self):
        self.question_canvas.config(bg="white")
        if self.quiz.still_has_questions():
            question = self.quiz.next_question()
            self.question_canvas.itemconfig(self.question_text, text=question)
        else:
            self.question_canvas.itemconfig(
                self.question_text, text="You have reached to the end of the quiz")
            self.right_button.config(state=DISABLED)
            self.wrong_button.config(state=DISABLED)

    def check_right_button(self):
        score, check = self.quiz.check_answer("True")
        self.score_label.config(text=f"Score {score}")
        self.feedback(check)

    def check_wrong_button(self):
        score, check = self.quiz.check_answer("False")
        self.score_label.config(text=f"Score {score}")
        self.feedback(check)

    def feedback(self, check: bool):
        if check:
            self.question_canvas.config(bg="green")
        else:
            self.question_canvas.config(bg="red")
        self.window.after(1000, self.canvas_question)
