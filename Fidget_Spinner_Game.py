from turtle import *

#This is the angle of the turn
state = {'turn': 0}

def spinner():
    clear()

    #Set the angle for the movement
    angle = state['turn'] / 10

    #Draw the red dot
    right(angle)
    forward(100)
    dot(120, 'red')
    back(100)

    #Draw the Green Dot
    right(120)
    forward(100)
    dot(120, 'green')
    back(100)

    #Draw the blue Dot
    right(120)
    forward(100)
    dot(120, 'blue')
    back(100)


    right(120)
    update()

def animate():
    if state['turn'] > 0:
        state['turn'] -= 1

    spinner()
    ontimer(animate, 20)

def flick():
    state['turn'] += 10

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
width(20)
onkey(flick, 'space')
listen()
animate()
done()
