from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score
import time
import tkinter
screen=Screen()
screen.setup(600,600)
screen.title('my snake game')
screen.bgcolor('orange')
screen.tracer(0)

score=Score()
snake=Snake()
food=Food()

screen.listen()

screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_on=True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    score.update_scoreboard()

    if snake.head.distance(food) < 18:
        food.refresh()
        snake.extend()
        score.increase_score()

    if snake.head.xcor() < -295 or snake.head.xcor() > 295 or snake.head.ycor() < -295 or snake.head.ycor() > 295 :
        score.reset()
        snake.reset()
        box=tkinter.messagebox.askokcancel("Game Over", "You hit the wall! Game Over!")
        if box==False:
            game_on=False
            screen.clear()
            screen.bgcolor('blue')


    for i in snake.segments[1:]:
        if snake.head.distance(i)<10:
            score.reset()
            snake.reset()

screen.exitonclick()