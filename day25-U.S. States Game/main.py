import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

tim = turtle.Turtle()
tim.penup()
tim.hideturtle()

score = 0
game_ongoing = True
guessed = set()
states = pd.read_csv("50_states.csv")

def check_guess(answer_state: str) -> bool:
    if not answer_state:
        return False
    answer_state = answer_state.strip().title()
    if answer_state in guessed:
        return False

    row = states[states.state == answer_state]
    if row.empty:
        return False

    x = int(row.iloc[0].x)
    y = int(row.iloc[0].y)

    tim.goto(x, y)
    tim.write(answer_state)
    guessed.add(answer_state)
    return True

while game_ongoing:
    answer_state = screen.textinput(title=f"{len(guessed)}/50 States Correct", prompt="What is another state? (type Exit to quit)")

    if not answer_state or answer_state.lower() == "Exit":
        break

    if check_guess(answer_state):
        score += 1
        if score == 50:
            game_ongoing = False

screen.exitonclick()


