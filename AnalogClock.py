from turtle import*
import time
time.time()
t = Turtle()
wn = Screen()
wn.title("Simple Analog Clock")
wn.bgcolor("black")
wn.setup(600,600)
t.speed(1)
t.pensize(3)
t.hideturtle()
wn.tracer(0)

def draw_clock(h,m,s,t):
    t.penup()
    t.goto(0,210)
    t.setheading(180)
    t.pencolor("green")
    t.pendown()
    t.circle(210)

    # Draw the clock marking for hand hour
    t.penup()
    t.goto(0,0)
    t.setheading(90)
    for _ in range(12):
        t.forward(190)
        t.pendown()
        t.fd(28)
        t.penup()
        t.goto(0,0)
        t.right(30)

    # Draw the clock marking for minute and second hours
    t.penup()
    t.goto(0, 0)
    t.setheading(90)
    for _ in range(60):
        t.forward(200)
        t.pendown()
        t.fd(10)
        t.penup()
        t.goto(0, 0)
        t.right(6)

    # Draw number on clock face
    # one
    t.penup()
    t.goto(0, 0)
    t.setheading(60)
    t.fd(145)
    t.setheading(0)
    t.fd(15)
    t.write(1,move=False,align="center",font=("arial",20,"normal"))

    # Two
    t.penup()
    t.goto(0, 0)
    t.setheading(30)
    t.fd(135)
    t.setheading(0)
    t.fd(35)
    t.write(2,move=False,align="center",font=("arial",20,"normal"))

    # Three
    t.penup()
    t.goto(0, 0)
    t.setheading(352)
    t.fd(150)
    t.setheading(0)
    t.fd(25)
    t.write(3,move=False,align="center",font=("arial",20,"normal"))

    # four
    t.penup()
    t.goto(0, 0)
    t.setheading(315)
    t.fd(150)
    t.setheading(0)
    t.fd(45)
    t.write(4,move=False,align="center",font=("arial",20,"normal"))

    # five
    t.penup()
    t.goto(0, 0)
    t.setheading(290)
    t.fd(178)
    t.setheading(0)
    t.fd(25)
    t.write(5,move=False,align="center",font=("arial",20,"normal"))

    # six
    t.penup()
    t.goto(0, 0)
    t.setheading(270)
    t.fd(190)
    t.write(6,move=False,align="center",font=("arial",20,"normal"))

    # seven
    t.penup()
    t.goto(0, 0)
    t.setheading(258)
    t.fd(170)
    t.setheading(180)
    t.fd(48)
    t.write(7,move=False,align="center",font=("arial",20,"normal"))

    # eight
    t.penup()
    t.goto(0, 0)
    t.setheading(228)
    t.fd(150)
    t.setheading(180)
    t.fd(45)
    t.write(8,move=False,align="center",font=("arial",20,"normal"))

    # nine
    t.penup()
    t.goto(0, 0)
    t.setheading(188)
    t.fd(150)
    t.setheading(180)
    t.fd(25)
    t.write(9,move=False,align="center",font=("arial",20,"normal"))

    # ten
    t.penup()
    t.goto(0, 0)
    t.setheading(150)
    t.fd(135)
    t.setheading(180)
    t.fd(25)
    t.write(10,move=False,align="center",font=("arial",20,"normal"))

    # eleven
    t.penup()
    t.goto(0, 0)
    t.setheading(120)
    t.fd(145)
    t.setheading(180)
    t.fd(15)
    t.write(11,move=False,align="center",font=("arial",20,"normal"))

    # twelve
    t.penup()
    t.goto(0, 0)
    t.setheading(90)
    t.fd(150)
    t.write(12,move=False,align="center",font=("arial",20,"normal"))

    # Draw hour hand
    t.pu()
    t.goto(0, 0)
    t.pencolor("white")
    t.setheading(90)
    angle = (h/12)*360
    t.rt(angle)
    t.pendown()
    t.fd(80)

    # Draw minute hand
    t.pu()
    t.goto(0, 0)
    t.pencolor("blue")
    t.setheading(90)
    angle = (m/60)*360
    t.rt(angle)
    t.pendown()
    t.fd(120)

    # Draw second hand
    t.pu()
    t.goto(0, 0)
    t.pencolor("yellow")
    t.setheading(90)
    angle = (s/60)*360
    t.rt(angle)
    t.pendown()
    t.fd(160)
    
    # Design by
    t.penup()
    t.goto(0, 0)
    t.pencolor("red")
    t.setheading(268)
    t.fd(125)
    t.setheading(0)
    t.fd(5)
    t.write("www.pj.com",move=False,align="center",font=("arial",18,"normal"))


while True:
    h = int(time.strftime("%I"))
    m = int(time.strftime("%M"))
    s = int(time.strftime("%S"))
    draw_clock(h,m,s,t)
    wn.update()
    time.sleep(1)    
    t.clear()
mainloop()