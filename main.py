from turtle import Screen, Turtle
import time
from food import Food
from snake import Snake
from score import Scoreboard

screen = Screen()
screen.setup(width=700, height=700)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

# create border
WALL = 300
border = Turtle()
border.penup()
border.color("orange")
border.hideturtle()
border.goto(-310, 310)
border.pendown()
for _ in range(4):
    border.forward(620)
    border.right(90)
score = Scoreboard()
food = Food()

snake = Snake()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        score.increase_score()
        snake.extend()

    if snake.head.xcor() > 310 or snake.head.xcor() < -310 or snake.head.ycor() > 310 or snake.head.ycor() < -310:
        score.game_over()
        game_is_on = False

    # Detect collision with tail
    for segment in snake.segments[1:]:
        # If head collides with any segment in the tall:
        if snake.head.distance(segment) < 5:
            # trigger game_over
            game_is_on = False
            score.game_over()

screen.exitonclick()
