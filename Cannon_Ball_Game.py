from random import randrange
from turtle import *
from base import vector

#Initial position of the ball
ball = vector(-200, -200)

#Intial change in the position of the ball
speed = vector(0, 0)

#Initial list of targets
targets = []

#Function to be called when user Click the screen
def tap(x, y):
    "Respond to screen tap."

    #This is to check wheather the ball is not in the screen or not.
    #If not then it will change the position of the ball with the values of the speed.
    if not inside(ball):
        ball.x = -199
        ball.y = -199
        speed.x = (x + 200) / 25
        speed.y = (y + 200) / 25

#This is a inside function to check the ball is in screen or not. It just returns true and false.
def inside(xy):
    "Return True if xy within screen."
    return -200 < xy.x < 200 and -200 < xy.y < 200

#This is the function to draw the ball and the targets.
def draw():
    "Draw ball and targets."
    clear()

    #This is the for loop to set the values for the targets like size and color.
    for target in targets:
        goto(target.x, target.y)
        dot(20, 'blue')

    #This is conditional statement that if the ball is inside screen the turtle will go to that position and
    #will create a dot as a ball.
    if inside(ball):
        goto(ball.x, ball.y)
        dot(6, 'red')
    #This is to just update the screen after every change.
    update()

#This function is for the movement of the ball and the targets.
def move():
    "Move ball and targets."

    #For the targets only y position will be changed and the targets will move from right to left.
    if randrange(40) == 0:
        y = randrange(-150, 150)
        target = vector(200, y)
        targets.append(target)
        
    #For the targets to move with this speed to the left.
    for target in targets:
        target.x -= 0.5

    #For the ball to move in the screen and basically to get the ball down.
    #If we don't do this then the ball will never come down like a cannon
    if inside(ball):
        speed.y -= 0.35
        ball.move(speed)

    #This line of code is just to copy the targets and have multiple targets coming.
    dupe = targets.copy()
    targets.clear()

    #This line of code is just to check if the position of ball and target become same then we make the target disapper.
    for target in dupe:
        if abs(target - ball) > 13:
            targets.append(target)

    #This is just a call to the draw function.
    draw()


    #This is to check that if targets are still inside screen or not.
    #Basically to check if the game is over or not. It returns nothing and game Over.
    for target in targets:
        if not inside(target):
            return

    ontimer(move, 50)

setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
done()
