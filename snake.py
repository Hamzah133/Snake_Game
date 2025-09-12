from token import LEFTSHIFT
import turtle
from turtle import Turtle

turtle.colormode(255) 
START_POSITIONS= [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE=20
UP=90
DOWN=270
LEFT=180
RIGHT=0
class Snake:
    def __init__(self):
        self.segments = []
        self.count=0
        self.switch=True
        self.create_snake()
        self.head = self.segments[0]
        

    def create_snake(self):
        for i in START_POSITIONS:
            self.add_segment(i)

    def add_segment(self,position):
        my_turtle = Turtle('square')
        if self.count>=220:
            self.switch=False
        elif self.count<=30:
            self.switch=True
        if self.switch:
            self.count+=30
        else:
            self.count-=30
        if len(self.segments)==0:
            my_turtle.color('red')
        else:
            my_turtle.color((self.count,self.count,self.count))
        my_turtle.penup()
        my_turtle.goto(position)
        self.segments.append(my_turtle)

    def reset(self):
        for i in self.segments:
            i.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]



    def extend(self):
        self.add_segment(self.segments[-1].position())
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading()!=DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)