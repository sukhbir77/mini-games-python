

from turtle import *
from random import randrange
from base import square, vector

#This is the food defined using a vector.
food = vector(0, 0)

#This is snake defined using again the vector and the list.
#List is used because the length of the snake will increase.
snake = [vector(10, 0)]

#This is for changing the direction of the snake and it will move downwards initally.
aim = vector(0, -10)

#This function is for the functionality of the game to move the snake.
def change(x, y):
    #This is to change the direction of the snake.
    aim.x = x
    aim.y = y

#This function is just to check if the snake hits the boundary or not.
def inside(head):
    return -200 < head.x < 190 and -200 < head.y < 190

#This function is usually for the movement of the snake and logic behind the game.
def move():

    #This is to copy the last position of the snake and to assign it as a head of the snake.
    head = snake[-1].copy()
    head.move(aim)

    #This is to check if the snake has hit himself or not.
    #If it hits himself then turn the color of the head of the snake to red.
    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    #This line is just change the head as the snake moves.
    #Poped element will go to the last and becomes the head of the snake.
    snake.append(head)

    #This is to check if the snake has eaten the food or not.
    #Means if the food becomes the head of the snake while it moves through the food.
    if head == food:
        
        print('Snake:', len(snake))
        #This line is just to create the another food randomly
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    #This is just the movement of the snake that if it doesn't eat the food then moves the snake.
    else:
        snake.pop(0)

    clear()

    #This is for the body of the snake.
    for body in snake:
        square(body.x, body.y, 9, 'black')
    #This is just for the body of the food.
    square(food.x, food.y, 9, 'green')
    update()
    ontimer(move, 70)

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()
