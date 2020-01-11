"""
Snake Game
Created by: Fahim Kamal
Date: 11.01.2020
"""
import turtle
import time
import random


delay = 0.1
# Setup the Screen
window = turtle.Screen()
window.title('Snake Game by Fahim Kamal')
window.bgcolor('blue')
window.setup(width=600, height=600)
window.tracer()

# Snake Head
snake_head = turtle.Turtle()
snake_head.speed(0)
snake_head.shape('square')
snake_head.color('black')
snake_head.penup()
snake_head.goto(0, 0)
snake_head.direction = 'stop'

# Snake Food
snake_food = turtle.Turtle()
snake_food.speed(0)
snake_food.shape('circle')
snake_food.color('red')
snake_food.penup()
snake_food.goto(0, 0)

# Functions
def go_up():
    snake_head.direction = 'up'

def go_down():
    snake_head.direction = 'down'

def go_right():
    snake_head.direction = 'right'

def go_left():
    snake_head.direction = 'left'

def move():
    if snake_head.direction == 'up':
        snake_head.sety(snake_head.ycor() + 20)
    if snake_head.direction == 'down':
        snake_head.sety(snake_head.ycor() - 20)
    if snake_head.direction == 'right':
        snake_head.setx(snake_head.xcor() + 20)
    if snake_head.direction == 'left':
        snake_head.setx(snake_head.xcor() - 20)


# Key bindings
window.listen()
window.onkeypress(go_up, key= 'Up')
window.onkeypress(go_down, key= 'Down')
window.onkeypress(go_right, key= 'Right')
window.onkeypress(go_left, key= 'Left')

# Main loop
while True:
    window.update()
    # distance() function calculates the distance of two turtles
    if snake_head.distance(snake_food) < 20:
        # Move the food to a random location
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        snake_food.goto(x, y)

    move()
    # the sleep() functions delays given amount of time to execute
    time.sleep(delay)
