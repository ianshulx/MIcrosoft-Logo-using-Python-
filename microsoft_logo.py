import turtle

hcore=turtle.Turtle()
hcore.speed(5)
hcore.color("#F65314")

hcore.begin_fill()
hcore.penup()
hcore.goto(-250,200)
hcore.pendown()
for i in range (4):
    hcore.forward(100)
    hcore.right(90)
hcore.end_fill()


hcore.color("#7CBB00")
hcore.begin_fill()
hcore.penup()
hcore.goto(-140,200)
hcore.pendown()
for i in range (4):
    hcore.forward(100)
    hcore.right(90)
hcore.end_fill()


hcore.color("#FFBB00")
hcore.begin_fill()
hcore.penup()
hcore.goto(-140,90)
hcore.pendown()
for i in range (4):
    hcore.forward(100)
    hcore.right(90)
hcore.end_fill()


hcore.color("#00A1F1")
hcore.begin_fill()
hcore.penup()
hcore.goto(-250,90)
hcore.pendown()
for i in range (4):
    hcore.forward(100)
    hcore.right(90)
hcore.end_fill()


hcore.pencolor("black")
hcore.penup()
hcore.goto(-25,50)
hcore.pendown()
hcore.pensize(12)
hcore.write("Microsoft",font=("calbri",50,"bold"))

hcore.hideturtle()

turtle.done()
