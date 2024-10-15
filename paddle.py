from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,x_cor,y_cor):
        super().__init__()
        self.x_cor=self.xcor()
        self.y_cor=self.ycor()
        self.shape('square')
        self.shapesize(6,1)
        self.penup()
        self.goto(x_cor,y_cor)
        self.speed("fastest")


    #to move paddle upwards
    def up_func(self):
        new_y = self.ycor()+20
        self.goto(self.xcor(),new_y)

    #to move paddle downward
    def down_func(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)






