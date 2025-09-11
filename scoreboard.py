from turtle import Turtle, Screen


class Score(Turtle):
    def __init__(self):
        super().__init__()

        with open('data.txt', 'r') as f:
            self.highscore = int(f.read())
        self.score = 0
        self.penup()
        self.color('black')
        self.hideturtle()
        self.goto(0,270)
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        self.write(f'Score: {self.score} Highscore: {self.highscore}', False, 'center', ('Arial', 16, 'bold'))

    def reset(self):
        if self.score > self.highscore:
            with open('data.txt','w') as f:
                f.write(f'{self.score}')
            self.highscore = self.score
        self.score=0
        self.update_scoreboard()


    def increase_score(self):
        self.score += 1
        self.update_scoreboard()


    def game_over(self):
        self.goto(0, 0)
        self.write('GAME OVER', False, 'center', ('Arial', 25, 'bold'))
# turtle=Score()
# # turtle.new_score()
#
# screen=Screen()
# screen.exitonclick()