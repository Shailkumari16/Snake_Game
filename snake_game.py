import turtle
import time
import random

speed=0.1

score=0
high_score=0

scr=turtle.Screen()
scr.title("Snake game")
scr.bgcolor("#0f274d")
scr.setup(width=600, height=600)
scr.tracer(0)

#snake head
top=turtle.Turtle()
top.speed(0)
top.shape("square")
top.color("#edeff2")
top.penup()
top.goto(0,0)
top.direction="stop"

#target

target=turtle.Turtle()
target.speed(0)
target.shape("square")
target.color("#cc0e2b")
target.penup()
target.goto(0,100)

body=[]

pen=turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("#deff05")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("score: 0   high score: 0",align="center",font=("courier",24,"normal"))


def move():
    if top.direction=="up":
        y=top.ycor()
        top.sety(y+20)

    if top.direction=="down":
        y=top.ycor()
        top.sety(y-20)
    
    if top.direction=="left":
        x=top.xcor()
        top.setx(x-20)

    if top.direction=="right":
        x=top.xcor()
        top.setx(x+20)

def up():
    if top.direction!='down':
        top.direction='up'

def down():
    if top.direction!='up':
        top.direction='down'


def left():
    if top.direction!='right':
        top.direction='left'


def right():
    if top.direction!='left':
        top.direction='right'

scr.listen()

scr.onkey(up, "Up")  
scr.onkey(down, "Down")
scr.onkey(left, "Left")
scr.onkey(right, "Right")




#main part
while True:
    scr.update()

    if top.xcor()>290 or top.xcor()<-290 or top.ycor()>290 or top.ycor()<-290:
        time.sleep(1)
        top.goto(0,0)
        top.direction='stop'
        for item in body:
            item.goto(1000, 1000)
        
        
        score=0
        speed=0.1
        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal")) 
        

    if top.distance(target) < 20:
        x1=random.randint(-280,280)
        y1=random.randint(-280,280)
        target.goto(x1,y1)

        box=turtle.Turtle()
        box.speed()
        box.shape("square")
        box.color("#edeff2")
        box.penup()
        body.append(box)
        score+=1
        speed-=0.001

        if score>high_score:
            high_score=score
        pen.clear()
        pen.write(f"score: {score}   high_score: {high_score}",align="center",font=("courier",24,"normal"))

    
    for i in range(len(body)-1,0,-1):
        x=body[i-1].xcor()
        y=body[i-1].ycor()
        body[i].goto(x, y)
    if len(body)>0:
        x=top.xcor()
        y=top.ycor()
        body[0].goto(x, y)

    move()

    for item in body:
        if item.distance(top)<20:
            time.sleep(1)
            top.goto(0,0)
            top.direction='stop'
            for item in body:
                item.goto(1000, 1000)
        
            body.clear()
            score=0
            speed=0.1
            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal")) 


    time.sleep(0.1)

scr.mainloop()