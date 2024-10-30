import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# answer_state = screen.textinput(title= "Guess the State", prompt= "What's the name of another state?").title()
data = pandas.read_csv("50_states.csv")
all_states = data.state

correct_states = []

# Function to get the state name and print it on the map
def print_state_name(state_name):
    state_data = data[data.state == state_name]
    if not state_data.empty:
        x = state_data.x.values[0]
        y = state_data.y.values[0]
        writer = turtle.Turtle()
        writer.hideturtle()
        writer.penup()
        writer.goto(x, y)
        writer.write(state_name, align="center", font=("Arial", 10, "normal"))

# Main game loop
while len(correct_states) < 51:
    len_correct_states = len(correct_states)
    answer_state = screen.textinput(title= str(len_correct_states) + "/50 States correct",
                                    prompt= "What's the name of another state?").title()
    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in correct_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in all_states:
        correct_states.append(answer_state)
        print_state_name(answer_state)
