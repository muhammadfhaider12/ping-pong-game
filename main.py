import time
from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard


paddle_r=Paddle(380,0)
paddle_l=Paddle(-380,0)
ball=Ball()
scoreboard=Scoreboard()
screen= Screen()
screen.tracer(0)

screen.setup(800,800)
screen.listen()
screen.onkey(paddle_r.up_func,"Up")
screen.onkey(paddle_r.down_func,"Down")

screen.onkey(paddle_l.up_func,"w")
screen.onkey(paddle_l.down_func,"s")


game_is_on=True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor()>380 or ball.ycor()<-380:
        ball.bounce_y()

    if ball.distance(paddle_r)<70 and ball.xcor()>350 or ball.distance(paddle_l)<70 and ball.xcor() < -350:
        ball.bounce_x()

    if ball.xcor()>390:
        ball.reset_func()
        scoreboard.l_score_sc()

    if ball.xcor() < -390:
        ball.reset_func()
        scoreboard.r_score_sc()

    if scoreboard.l_score==10:
        scoreboard.game_over()
        scoreboard.left_win()
        game_is_on=False

    if scoreboard.r_score==10:
        scoreboard.game_over()
        scoreboard.right_win()
        game_is_on = False



screen.exitonclick()
