from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake game")

# turn off tracer
screen.tracer(0)

# create a snake object
snake = Snake()

# create a food object
food = Food()

# create a score object
score = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
game_is_on = True

# to automatically move the snake
while game_is_on:
    # if we update screen here, the screen updates after all the segments move
    screen.update()
    time.sleep(0.1)
    snake.move()

    # detect collision with food
    if snake.head.distance(food) < 20:
        # then refresh the location of food
        food.generate_food()
        # and update the score
        score.update_score()
        # extend length of the snake
        snake.extend()

    # detect collision with wall
    if snake.head.xcor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -300:
        # print game over on the screen
        score.game_over()
        # stop the game
        game_is_on = False

    # detect collision with own tail
    # if head collides with any segment, game over
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()

screen.exitonclick()
