from turtle import Screen
import snake
import time
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.title("The Snake Game")
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)


game_snake = snake.Snake()
food = Food()
score = ScoreBoard()

screen.listen()
screen.onkeypress(fun=game_snake.up, key="Up")
screen.onkeypress(fun=game_snake.down, key="Down")
screen.onkeypress(fun=game_snake.turn_left, key="Left")
screen.onkeypress(fun=game_snake.turn_right, key="Right")


game_is_on = True
while game_is_on:
    head = game_snake.segment_list[0]
    game_snake.move()
    time.sleep(0.1)

# CHECKING FOOD COLLISION, SCORE UPDATE, SEGMENT EXTENSION
    if head.distance(food) < 15:
        food.refresh()
        score.update_score()
        game_snake.add_food_segment()

# CHECKING BORDER COLLISION
    if head.xcor() > 280 or head.xcor() < -280 or head.ycor() > 280 or head.ycor() < -280:
        score.reset_game()
        game_snake.put_snake_away()

# CHECKING  BODY COLLISION
    for segment in game_snake.segment_list[1:]:
        if head.distance(segment) < 10:
            score.reset_game()
            game_snake.put_snake_away()
    screen.update()

screen.exitonclick()
