import turtle
import pandas

screen = turtle.Screen()
screen.title('U.S States Game')
background = 'blank_states_img.gif'
screen.addshape(background)
turtle.shape(background)

data = pandas.read_csv('50_states.csv')
states = data.state.to_list()
answers = []

while len(answers) < 50:
    answer_state = screen.textinput(title=f'{len(answers)}/50 States Correct',
                                    prompt='What\'s another state\'s name?').title()
    if answer_state == 'Exit':
        missing = set(states).difference(answers)
        to_save = pandas.DataFrame(missing)
        to_save.to_csv('states_to_learn.csv')
        break
    if answer_state in states:
        answers.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        found_state = data[data.state == answer_state]
        t.goto(int(found_state.x), int(found_state.y))
        t.write(found_state.state.item())
