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

# Snake Body segment
snake_body_segment = []

# Snake Food
snake_food = turtle.Turtle()
snake_food.speed(0)
snake_food.shape('circle')
snake_food.color('red')
snake_food.penup()
snake_food.goto(0, 100)

# Pen to show score
score = 0
high_score = 0
pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write(f'Score: {score}  High score: {high_score}', align='center', font=('Arial', 20, 'bold'))


# Functions
def go_up():
    if snake_head.direction != 'down':
        snake_head.direction = 'up'


def go_down():
    if snake_head.direction != 'up':
        snake_head.direction = 'down'


def go_right():
    if snake_head.direction != 'left':
        snake_head.direction = 'right'


def go_left():
    if snake_head.direction != 'right':
        snake_head.direction = 'left'


def move():
    """Controls the snakes movements"""
    if snake_head.direction == 'up':
        snake_head.sety(snake_head.ycor() + 20)
    if snake_head.direction == 'down':
        snake_head.sety(snake_head.ycor() - 20)
    if snake_head.direction == 'right':
        snake_head.setx(snake_head.xcor() + 20)
    if snake_head.direction == 'left':
        snake_head.setx(snake_head.xcor() - 20)


def create_body():
    """Create's a new body-part and add with head"""
    new_body_part = turtle.Turtle()
    new_body_part.speed(0)
    new_body_part.shape('circle')
    new_body_part.color('grey')
    new_body_part.penup()
    snake_body_segment.append(new_body_part)


def die():
    """The snake will die and reset"""
    time.sleep(1)
    snake_head.goto(0, 0)
    snake_head.direction = 'stop'

    # Hide the segments
    for part in snake_body_segment:
        part.goto(1000, 1000)
    # Clear the segment list
    snake_body_segment.clear()

def show_score():
    pen.clear()
    pen.write(f'Score: {score}  High score: {high_score}', align='center', font=('Arial', 20, 'bold'))


# Key bindings
window.listen()
window.onkeypress(go_up, key='Up')
window.onkeypress(go_down, key='Down')
window.onkeypress(go_right, key='Right')
window.onkeypress(go_left, key='Left')

# Main loop
while True:
    window.update()
    # Check for collision with the border
    if snake_head.ycor() < -290 or snake_head.ycor() > 290 or snake_head.xcor() < -290 or snake_head.xcor() > 290:
        die()
        # Reset the score
        score = 0
        show_score()


    # distance() function calculates the distance of two turtles
    # Check for a collision with the food
    if snake_head.distance(snake_food) < 20:
        # Move the food to a random location
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        snake_food.goto(x, y)
        delay -= 0.002

        # Increase the score
        score += 10
        if score > high_score:
            high_score = score
        show_score()

        # Create a segment for the the body
        create_body()

    # Move the last segment first in reverse order
    for index in range(len(snake_body_segment) - 1, 0, -1):
        # Get the x and y coordinate of the segment that is before the current segment
        x = snake_body_segment[index - 1].xcor()
        y = snake_body_segment[index - 1].ycor()
        # And move to that location
        snake_body_segment[index].goto(x, y)

    # Move the body_segment to where the head was
    if len(snake_body_segment):
        x = snake_head.xcor()
        y = snake_head.ycor()
        snake_body_segment[0].goto(x, y)
    # The movement of the snake head according to user input
    move()

    # Check body collision
    for segment in snake_body_segment:
        if segment.distance(snake_head) < 20:
            die()
            # Reset the score
            score = 0
            show_score()
            break

    # the sleep() functions delays given amount of time to execute
    time.sleep(delay)
