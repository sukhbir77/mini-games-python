from random import choice, random
from turtle import *
from base import vector

#This will generate a random value between (-5,-3) or (3,5)
def value():
    return (3 + random() * 2) * choice([1, -1])

#Ball is defined here
ball = vector(0, 0)

#Initial movement of the ball is random
aim = vector(value(), value())
state = {1: 0, 2: 0}

#Move the player
def move(player, change):
    state[player] += change

#To draw the players or Pong. Basically Players will be rectangular
def rectangle(x, y, width, height):
    up()
    goto(x, y)
    down()    
    begin_fill()
    color('RED')
    for count in range(2):
        forward(width)
        left(90)
        forward(height)
        left(90)
    end_fill()

#To draw the game board and the pong ball.
def draw():
    
    clear()
    #Two players are drawn first.
    rectangle(-200, state[1], 10, 50)
    rectangle(190, state[2], 10, 50)

    #Then the ball is moved with the initial change in the direction.
    ball.move(aim)
    x = ball.x
    y = ball.y

    up()
    goto(x, y)
    dot(10)
    update()

    #To change the direction of the ball when it hits the top or bottom of the game board.
    if y < -200 or y > 200:
        aim.y = -aim.y
    
    #To change the direction of the ball when it hits the Player 1.
    if x < -185:
        low = state[1]
        high = state[1] + 50

        if low <= y <= high:
            aim.x = -aim.x
        else:
            return
        
    #To change the direction of the ball when it hits the Player 2.
    if x > 185:
        low = state[2]
        high = state[2] + 50

        if low <= y <= high:
            aim.x = -aim.x
        else:
            return
    #To Update
    ontimer(draw, 50)

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: move(1, 20), 'w')
onkey(lambda: move(1, -20), 's')
onkey(lambda: move(2, 20), 'i')
onkey(lambda: move(2, -20), 'k')
draw()
done()
