import turtle

import pandas as pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

states_data = pandas.read_csv("50_states.csv")

# answer = screen.textinput(title="Guess the State", prompt="What's another state's name?")
# state = states_data[states_data.state == answer]
correct = 0
guess_dict = {}
state_turtle = turtle.Turtle()
state_turtle.hideturtle()
state_turtle.penup()

#
guessing = True
while guessing and correct < 50:
    answer = screen.textinput(title=f"{correct}/50 States Correct", prompt="What's another state's name?")
    if not answer or answer == "Exit":
        guessing = False
    else:
        answer = answer.title()
        state = states_data[states_data.state == answer]
        if not state.empty and answer not in guess_dict:
            x = state.iloc[0].x
            y = state.iloc[0].y
            correct += 1
            state_turtle.goto(x, y)
            state_turtle.write(state.iloc[0].state)
            guess_dict[answer] = True

all_states = states_data.state.to_list()
states_to_learn = [state_title for state_title in all_states if state_title not in guess_dict]

if len(states_to_learn) != 0:
    df = pandas.DataFrame({"states": states_to_learn})
    df.to_csv("states_to_learn.csv")
