import turtle
import time
import random 

delay = 0.1
# score
score = 0
high_score = 0

# set up the screen

wn = turtle.Screen()
wn.title("snake Game by @tokyoEdtech")
wn.bgcolor("green")
wn.setup(width=600, height=600)
wn.tracer(0)

# snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.penup()
head.goto(0,0)
head.direction = "stop"

# snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)

segments = []

# pen
pen = turtle.Turtle()
pen.speed(1)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("score: 0  High score: 0", align="center", font=("Courier",24,"normal"))

# functions

def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"


def go_left():
    if head.direction != "right":
        head.direction = "left"


def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.ycor()
        head.setx(x - 20)

    if head.direction == "up":
        x = head.ycor()
        head.setx(x + 20)

# Keyboard binding
wn.listen()
wn.onkeypress(go_up,"w")
wn.onkeypress(go_down,"s")
wn.onkeypress(go_left,"a")
wn.onkeypress(go_right,"d")

# Main game loop
while True:
    wn.update()

    # check for the collonsion with the border
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"

        # hide the elements
        for segment in segments:
            segment.goto(1000,1000)

        # clear the segments list
        segments.clear()

        # reset the score
        score = 1

        # Reset the delay
        delay = 0.1

        pen.clear()
        pen.write("score: {} High score: {}".format(score, high_score), align="center", font=("Courier",24,"normal"))

    # check for the collinsion with the food
    if head.distance(food) < 20:
        x = random.randint(-290,290)
        y = random.randint(-290,290)
        food.goto(x,y)

        # Add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

        # shorten the delay
        delay -= 0.001

        # Increse the score 
        score += 10

        if score > high_score:
            high_score = score

        pen.clear()
        pen.write("score: {} High score: {}".format(score,high_score),align="center",font=("Courier",24,"normal"))  

    # move the segments first in reverse order
    for index in range(len(segments)-1,0,-1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x,y)

    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)

    move()

    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(0)
            head.goto(0,0)
            head.direction = "stop"

            for segment in segments:
                segment.goto(1000,1000)

            segments.clear()

            score = 0

            delay = 0.1

            pen.clear()
            pen.write("score: {} High score: {}".format(score,high_score),align="center",font=("Courier",24,"normal"))

    time.sleep(delay)
    wn.mainloop()                
                    

