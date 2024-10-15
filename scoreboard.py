from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
         super().__init__()
         self.hideturtle()
         self.penup()
         self. l_score=0
         self.r_score=0
         self.goto(-100,300)
         self.write(self.l_score,align="center",font=("Courier",80, "normal"))
         self.goto(100, 300)
         self.write(self.r_score, align="center", font=("Courier", 80, "normal"))
         self.update_score()
    def update_score(self):
        self.clear()
        self.goto(-100, 300)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 300)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))

    def l_score_sc(self):
        self.l_score +=1
        self.update_score()


    def r_score_sc(self):
        self.r_score += 1
        self.update_score()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER",align="center", font=("Courier",80, "normal"))

    def left_win(self):
        self.goto(0,-40)
        self.write("Left Team Won!", align="center", font=("Courier", 30, "normal"))


    def right_win(self):
        self.goto(0, -40)
        self.write("Right Team Won!", align="center", font=("Courier", 30, "normal"))
