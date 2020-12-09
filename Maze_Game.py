from random import*
from turtle import*
from base import line

#This is the draw function to draw the maze only.
def draw():
     #This is just to set the color of the lines of the maze.
    color('Black')
    #This is used to set the width of the lines of the maze.
    width(5)

    #This for loop is used to create the horizontal lines means x lines.
    for x in range(-400,400,40):
        #THis for loop is to create the vertical lines or along y axis.
        for y in range(-400,400,40):

            #create a matrix
            if random() > 0.5:
                line(x,y,x+40,y+40)
            else:
                line(x,y+40,x+40,y)
    update()

def tap(x,y):

    #This will draw a line and dot in the screen when you tap.
    if abs(x) > 398 or abs(y) > 398:
        up()
    else:
        down()
    width(2)
    color("Red")
    goto(x,y)
    dot(4)

setup(420,420,600,0)
hideturtle()
tracer(False)
draw()
onscreenclick(tap)
done()
