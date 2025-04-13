import turtle
import pandas

# Set up screen and background image
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Read data
data = pandas.read_csv("50_US_states.csv")
all_states = data.state.to_list()
guessed_states = []

# Helper turtle for messages
msg = turtle.Turtle()
msg.hideturtle()
msg.penup()
msg.goto(0, 270)
msg.write("Enter 'Exit' to quit the game.", align="center", font=("Arial", 16, "normal"))

# Game loop
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name?").title().strip()

    msg.clear()

    if answer_state == "":
        msg.write("Please enter a valid state name!", align="center", font=("Arial", 16, "normal"))

    elif answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        pandas.DataFrame(missing_states).to_csv("states_to_learn.csv")
        msg.goto(0, 250)
        msg.write("Game ended. Missing states saved to states_to_learn.csv", align="center", font=("Arial", 16, "normal"))
        break

    elif answer_state in guessed_states:
        msg.write(f"You already guessed {answer_state}!", align="center", font=("Arial", 16, "normal"))

    elif answer_state in all_states:
        guessed_states.append(answer_state)
        state_data = data[data.state == answer_state]
        writer = turtle.Turtle()
        writer.hideturtle()
        writer.penup()
        writer.goto(state_data.x.item(), state_data.y.item())
        writer.write(answer_state)
    else:
        msg.write(f"No state named '{answer_state}' found.", align="center", font=("Arial", 16, "normal"))
