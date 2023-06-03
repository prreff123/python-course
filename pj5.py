import turtle
t = turtle.Turtle()

# t.speed(200)
# turtle.bgcolor("black")

# for i in range(300):
#     t.color("yellow")
#     t.circle(i)
#     t.left(3)

# turtle.done()    
list =["green","red","purple","blue","cyan"]
turtle.bgcolor("black")
for i in range(200):
    t.color(list[i%5])
    t.pensize(i/10+1)
    t.forward(i)
    t.speed(20)
    t.left(50)

turtle.mainloop()    