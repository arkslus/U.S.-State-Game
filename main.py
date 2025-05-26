# import turtle module
import turtle

# import the panda module
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
screen.setup(width=720, height=480)
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


# read the csv file and store the states in a list
df = pd.read_csv("50_states.csv")
all_states = df["state"].to_list()

# create a list to store the guessed states
guessed_states = []


# play the game until all states are guessed
while len(guessed_states) < 50:
    answer_state = screen.textinput(
        title=f"{len(guessed_states)}/50 States Correct",
        prompt="What's another state's name?",
    ).title()

    # exit the game if the user enters "exit"
    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)

        # save the missing states to a new csv file
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    # check if the user's answer is correct and add it to the guessed states list
    if answer_state in all_states:
        guessed_states.append(answer_state)
        turt = turtle.Turtle()
        turt.hideturtle()
        turt.penup()
        state_data = df[df["state"] == answer_state]
        turt.goto(state_data["x"].item(), state_data["y"].item())
        turt.write(answer_state, align="center", font=("Arial", 8, "normal"))
        print(f"{answer_state} is correct!")
