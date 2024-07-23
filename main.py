from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snek gaem")
screen.tracer(0)
turtle_list = []
game_is_on = True

snake = Snake()
food = Food()
scoreboard = Scoreboard()

game_is_on = snake.game_state

food.refresh()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.turtle_list[0].distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.score_increase()

    if snake.turtle_list[0].xcor() > 280 or snake.turtle_list[0].ycor() > 280 or snake.turtle_list[0].xcor() < -280 or snake.turtle_list[0].ycor() < -280:
        scoreboard.reset()
        snake.reset()

    for i in range(len(snake.turtle_list)):
        if i == 0 or i == 1:
            pass
        elif snake.turtle_list[i].distance(snake.turtle_list[0]) < 10:
            scoreboard.reset()
            snake.reset()
screen.exitonclick()