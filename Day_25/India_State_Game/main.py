from turtle import *
import pandas

screen = Screen()
ALINGMENT = "center"
FONT = ("Arial", 14, "normal")
STATES = 29


def create_state(state_name, x_cor, y_cor):
    new_state = Turtle()
    new_state.penup()
    new_state.hideturtle()
    new_state.color("black")
    new_state.goto(x_cor, y_cor)
    new_state.write(f"{state_name}", align=ALINGMENT,
                    font=FONT)


def create_map():
    alex = Turtle()
    screen.setup(width=900, height=900)
    screen.title("India State Games")
    image = "india_map.gif"
    screen.addshape(image)
    alex.shape(image)


def main():
    total_correct_answers = 0
    game_is_on = True

    data = pandas.read_csv("state.csv")
    create_map()

    while game_is_on:
        answer_state = screen.textinput(title=f"{total_correct_answers}/{STATES} States Correct",
                                        prompt="What's another state name").title()
        if answer_state == 'Exit':
            break
        if answer_state in data.state.values:
            state_data = data[data.state == answer_state].iloc[0]
            total_correct_answers += 1
            create_state(state_data.state, state_data.x, state_data.y)

        if total_correct_answers == STATES:
            game_is_on = False


if __name__ == "__main__":
    main()

"""
#### Below is the code to get the mouse coordinates on the turtle screen which is the map
def get_coordinate(x, y):
    print(x, y)
turtle.onscreenclick(get_coordinate)
turtle.mainloop()
"""
