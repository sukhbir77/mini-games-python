from random import*
from turtle import*

from base import vector

#start of the vector
ant = vector(0,0)

#direction is used as a aim.
#First argument is the left(-ve) and right(+ve).
#Second argument is top(+ve) and bottom(-ve)
aim = vector(2,0)

def wrap(value):

    return value

def draw():
    ant.move(aim)
    ant.x = wrap(ant.x)
    ant.y = wrap(ant.y)
    aim.move(random()- 0.5)

    aim.rotate(random()*10-5)
    clear()

    goto(ant.x,ant.y)
    dot(15,'red')

    if running:
        ontimer(draw,100)
        
setup(420,420,370,0)
hideturtle()
tracer(False)
up()
running = True
draw()
done()
