import turtle
import pandas
screen=turtle.Screen()
screen.title("U.S. States Game")
image="blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
SCORE=0
CORRECT_GUESSES=[]
states_data=pandas.read_csv("50_states.csv")
states_list=states_data["state"].tolist()

def map_text(state_name,position):
    state_turtle=turtle.Turtle("classic")
    state_turtle.hideturtle()
    state_turtle.penup()
    state_turtle.goto(position)
    state_turtle.pendown()
    state_turtle.write(state_name)

while SCORE!=len(states_list):
    answer_state=screen.textinput(title=f"{SCORE}/50 States Correct",prompt="What is another state's name?").title()
    if answer_state=="Exit":
        missing_states=[]
        for state in states_list:
            if state not in CORRECT_GUESSES:
                missing_states.append(state)
        new_data=pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in states_list:
        if answer_state in CORRECT_GUESSES:
            pass
        else:
            CORRECT_GUESSES.append(answer_state)
            globals()
            SCORE=SCORE+1
            x_coor=states_data[states_data["state"]==answer_state]["x"].values[0]
            y_coor=states_data[states_data["state"]==answer_state]["y"].values[0]
            map_text(answer_state,(x_coor,y_coor))
