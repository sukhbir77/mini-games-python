from turtle import *
from base import square, vector

#Player 1 Settings
p1xy = vector(-100, 0)
p1aim = vector(4, 0)
p1body = set()

#Player 2 Settings
p2xy = vector(100, 0)
p2aim = vector(-4, 0)
p2body = set()

#To check if the players are inside the boundry.
def inside(head):
    return -200 < head.x < 200 and -200 < head.y < 200

#To draw the lines
def draw():

    #Movement for the player1 
    p1xy.move(p1aim)
    #Copy the head of the player1
    p1head = p1xy.copy()

    #Movement for the Player 2
    p2xy.move(p2aim)
    #Copy the head of the Player 2
    p2head = p2xy.copy()

    #Check if the Player 1 is inside the boundry and doesn't hit himself.
    if not inside(p1head) or p1head in p2body:
        print('Player blue wins!')
        return

    #Check if the Player 2 is inside the boundry and doesn't hit himself.
    if not inside(p2head) or p2head in p1body:
        print('Player red wins!')
        return

    #Add in the set with the player heads
    p1body.add(p1head)
    p2body.add(p2head)

    #Body Settings for the players
    square(p1xy.x, p1xy.y, 3, 'red')
    square(p2xy.x, p2xy.y, 3, 'blue')
    update()
    ontimer(draw, 100)

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
#Controls for the players
onkey(lambda: p1aim.rotate(90), 'a')
onkey(lambda: p1aim.rotate(-90), 'd')
onkey(lambda: p2aim.rotate(90), 'j')
onkey(lambda: p2aim.rotate(-90), 'l')
draw()
done()
