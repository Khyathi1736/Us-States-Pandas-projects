import turtle as t 
import pandas as pd
import time

screen=t.Screen()
image="blank_states_img.gif"
# to add new shape to the turtle 
screen.addshape(image)
# after added that shape we can access that shape 
timmy=t.Turtle()
timmy.shape(image)


# to print dataframe without row index 
# print(data.to_string(index=False))
data=pd.read_csv("50_US_states.csv")
all_states=data.state.to_list()

w=t.Turtle()
w.hideturtle()
k=t.Turtle()
k.hideturtle()
score=0
length=len(all_states)
for i in range(length):
    name=screen.textinput(title="Guess the State",prompt=f"What's another state name?   {score}/{length}").title()
    # name=name.capitalize()
    if score==length:
        k.goto(0,0)
        k.write("You guessed all states correctly")
        break 
      
    elif name=="Exit":
        break
    
    elif name in all_states:
        k.pu()
        row=data[data["state"]==name]
        k.goto(int(row.x),int(row.y))
        # k.write(row.state.item(),align="center",font=("Arial",8,"normal"))
        k.write(name,align="center",font=("Arial",10,"normal"))
        score+=1
    else:
        w.pu()
        w.clear()
        w.goto(10,280)
        w.write(f"No state named {name}",align="center",font=("Arial",20,"normal"))
 

screen.exitonclick()