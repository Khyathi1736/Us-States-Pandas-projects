import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_US_states.csv")
all_states = data.state.to_list()
guessed_states = []

h=turtle.Turtle()
h.hideturtle()
h.penup()
h.goto(10,280)
h.pendown()
h.write(f"enter exit to exit!",align="center",font=("Arial",20,"normal"))

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name?").title()
    if answer_state == "exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(answer_state)
    else:
        h.pu()
        h.clear()
        h.goto(10,280)
        h.write(f"No state named {answer_state}",align="center",font=("Arial",20,"normal"))
