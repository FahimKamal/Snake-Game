"""
Snake Game
Created by: Fahim Kamal
Date: 11.01.2020
"""
import turtle
import time
import random


delay = 0.05
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

# Snake Body segment
snake_body_segment = []

# Snake Food
snake_food = turtle.Turtle()
snake_food.speed(0)
snake_food.shape('circle')
snake_food.color('red')
snake_food.penup()
snake_food.goto(0, 100)

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
    # Check for a collision with the food
    if snake_head.distance(snake_food) < 20:
        # Move the food to a random location
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        snake_food.goto(x, y)

        # Create a segment for the the body
        new_body_part = turtle.Turtle()
        new_body_part.speed(0)
        new_body_part.shape('circle')
        new_body_part.color('grey')
        new_body_part.penup()
        snake_body_segment.append(new_body_part)

    # Move the last segment first in reverse order
    for index in range(len(snake_body_segment) - 1, 0, -1):
        # Get the x and y coordinate of the segment that is before the current segment
        x = snake_body_segment[index-1].xcor()
        y = snake_body_segment[index-1].ycor()
        # And move to that location
        snake_body_segment[index].goto(x, y)

    # Move the body_segment to where the head was
    if len(snake_body_segment):
        x = snake_head.xcor()
        y = snake_head.ycor()
        snake_body_segment[0].goto(x, y)
    move()
    # the sleep() functions delays given amount of time to execute
    time.sleep(delay)
