import turtle

SCORE_COORDINATES = (0, 270)
ALIGN = 'center'
FONT = ('arial', 18, 'normal')



class ScoreBoard(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.speed('fastest')
        self.goto(SCORE_COORDINATES)
        self.hideturtle()
        self.score = 0
        with open('high_score_data.txt', mode='r') as hs:
            self.high_score = int(hs.read())

    def update_score(self):
        self.clear()
        self.score += 1
        self.show_score()

    def show_score(self):
        self.write(arg=f"score = {self.score} | high score = {self.high_score}", move=False, align=ALIGN, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        with open('high_score_data.txt', mode='w') as hs:
            hs.write(f'{self.high_score}')
        self.score = 0
        self.clear()
        self.show_score()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(arg="game over", move=False, align=ALIGN, font=FONT)
