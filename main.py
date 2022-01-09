from turtle import Screen
from snake import Snake
from points import Food
from scoreboard import Scoreboard
import time

# Setting up the UI
screen = Screen()
screen.screensize(canvwidth=600, canvheight=600)
screen.setup(width=620, height=620)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

# Listens for keystrokes to control direction of snake
screen.listen()
screen.onkey(lambda: snake.turn_up(), 'Up')
screen.onkey(lambda: snake.turn_right(), 'Right')
screen.onkey(lambda: snake.turn_left(), 'Left')
screen.onkey(lambda: snake.turn_down(), 'Down')

snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.update()

game_play = True

while game_play:
    screen.update()
    time.sleep(0.1)

    snake.move()

    if snake.snake_head.distance(food) < 17:
        print("+1 point")
        food.relocate()
        snake.eaten_food()
        scoreboard.inc_score()
    if snake.over_bounds() | snake.collision():
        game_play = False
        scoreboard.game_over()
        print("Game over.")

screen.exitonclick()
