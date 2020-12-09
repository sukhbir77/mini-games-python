from random import *
from turtle import *
from base import floor, vector

#Tiles are defined empty
tiles = {}


#To draw the tiles we have this list of vectors
neighbors = [
    vector(100, 0),
    vector(-100, 0),
    vector(0, 100),
    vector(0, -100),
]

#To draw the Game Board of the game or the tiles.
def load():
    #This is just to keep the count of the tiles.get
    count = 1

    #Here we are drawing the tiles for the game.
    for y in range(-200, 200, 100):
        for x in range(-200, 200, 100):
            mark = vector(x, y)
            tiles[mark] = count
            count += 1

    #One tile should be empty in order to swap the tiles.
    tiles[mark] = None

    #To swap the tiles
    for count in range(1000):
        neighbor = choice(neighbors)
        spot = mark + neighbor

        if spot in tiles:
            number = tiles[spot]
            tiles[spot] = None
            tiles[mark] = number
            mark = spot

#To draw the tiles as squares.
def square(mark, number):
    
    up()
    goto(mark.x, mark.y)
    down()
    
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(99)
        left(90)
    end_fill()

    if number is None:
        return
    elif number < 10:
        forward(20)

    write(number, font=('Arial', 60, 'normal'))

#This function is just to swap the tiles when the user clicks on the tiles.
def tap(x, y):
    
    x = floor(x, 100)
    y = floor(y, 100)
    mark = vector(x, y)

    for neighbor in neighbors:
        spot = mark + neighbor

        if spot in tiles and tiles[spot] is None:
            number = tiles[mark]
            tiles[spot] = number
            square(spot, number)
            tiles[mark] = None
            square(mark, None)

#This is to draw all the tiles.
def draw():
    for mark in tiles:
        square(mark, tiles[mark])
    update()

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
load()
draw()
onscreenclick(tap)
done()
