import turtle
import time
import snake
import food
import score_board

screen = turtle.Screen()
score_board = score_board.ScoreBoard()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake game')

screen.tracer(0)

snake = snake.Snake()
food = food.Food()
score_board.show_score()

screen.listen()

screen.onkey(fun=snake.turn_up, key='Up')
screen.onkey(fun=snake.turn_down, key='Down')
screen.onkey(fun=snake.turn_left, key='Left')
screen.onkey(fun=snake.turn_right, key='Right')

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    # detect collision with food
    if snake.head.distance(food) < 15:
        food.spawn()
        score_board.update_score()
        snake.extends()

    # detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -300:
        score_board.reset()
        snake.reset()
        # game_is_on = False

    # detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            # game_is_on = False
            score_board.reset()
            snake.reset()


screen.exitonclick()
f