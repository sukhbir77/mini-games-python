from turtle import *
from base import line

#Create a game board to play
def grid():
    line(-67, 200, -67, -200)
    line(67, 200, 67, -200)
    line(-200, -67, 200, -67)
    line(-200, 67, 200, 67)

#Draw the x when the player taps.
def drawx(x, y):
    line(x, y, x + 133, y + 133)
    line(x, y + 133, x + 133, y)

#Draw the Y when the player taps
def drawo(x, y):
    up()
    goto(x + 67, y + 5)
    down()
    circle(62)

#Round value down to grid with square size 133
def floor(value):
    return ((value + 200) // 133) * 133 - 200

state = {'player': 0}
players = [drawx, drawo]

#This function will run when the screen is tapped
def tap(x, y):
    x = floor(x)
    y = floor(y)
    player = state['player']
    draw = players[player]
    draw(x, y)
    update()
    state['player'] = not player

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
grid()
update()
onscreenclick(tap)
done()
