import turtle
wn=turtle.Screen()
wn.bgcolor("blue")
wn.title("Ajay's ping pong game")
wn.setup(width=800,height=600)
wn.tracer()

score_1=0
score_2=0

#paddle 1
paddle1=turtle.Turtle()
paddle1.speed(0)
paddle1.shape("square")
paddle1.color("red")
paddle1.shapesize(stretch_wid=5,stretch_len=1)
paddle1.penup()
paddle1.goto(-350,0)

#paddle 2
paddle2=turtle.Turtle()
paddle2.speed(0)
paddle2.shape("square")
paddle2.color("green")
paddle2.shapesize(stretch_wid=5,stretch_len=1)
paddle2.penup()
paddle2.goto(350,0)

#ball
ball=turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx=2
ball.dy=2

#pen
pen=turtle.Turtle()
pen.speed(0)
pen.color("black")
pen.hideturtle()
pen.penup()
pen.goto(0,260)
pen.write("Player 1:0 || player2:0",align="center",font=("courier",24,"normal"))

def paddle_a_up():
    y=paddle1.ycor()
    y=y+20
    paddle1.sety(y)

def paddle_a_down():
    y=paddle1.ycor()
    y=y-20
    paddle1.sety(y)
    
def paddle_b_up():
    y=paddle2.ycor()
    y=y+20
    paddle2.sety(y)
    
def paddle_b_down():
    y=paddle2.ycor()
    y=y-20
    paddle2.sety(y)
    
wn.listen()
wn.onkeypress(paddle_a_up,"w")
wn.onkeypress(paddle_a_down,"s")
wn.onkeypress(paddle_b_up,"Up")
wn.onkeypress(paddle_b_down,"Down")

while True:
    wn.update()
    
#moving the  ball
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)
    
#bounce the ball
    if ball.ycor()>290:
        ball.sety(290)
        ball.dy=ball.dy*-1     
        
    if ball.ycor()<-290:
        ball.sety(-290)
        ball.dy=ball.dy*-1   
        
    if ball.xcor()>390:
        ball.goto(0,0)
        ball.dx=ball.dx*-1  
        pen.clear() 
        score_1=score_1+1
        pen.write("Player 1: {}|| player2: {}".format(score_1,score_2),align="center",font=("Courier",24,"normal"))
        
    if ball.xcor()<-390:
        ball.goto(0,0)
        ball.dx=ball.dx*-1  
        pen.clear() 
        score_2=score_2+1
        pen.write("Player 1: {}|| player2: {}".format(score_1,score_2),align="center",font=("Courier",24,"normal"))
           
#ball and paddles bounce
    if(ball.xcor() >340 and ball.xcor()<350) and (ball.ycor()<paddle2.ycor()+50 and ball.ycor()>paddle2.ycor()-50):
        ball.dx=ball.dx*-1
        
    if(ball.xcor() <-340 and ball.xcor()<-350) and (ball.ycor()<paddle1.ycor()+50 and ball.ycor()>paddle1.ycor()-50):
        ball.dx=ball.dx*-1
        
    
    

    



