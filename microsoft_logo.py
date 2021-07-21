import turtle
hc=turtle.Turtle()
hc.speed(4)

hc.color("#F65314")

hc.begin_fill()
hc.penup()
hc.goto(-250,200)
hc.pendown()

for i in range (4):
    hc.forward(100)
    hc.right(90)

hc.end_fill()
hc.color("#7CBB00")
hc.begin_fill()
hc.penup()
hc.goto(-140,200)
hc.pendown()

for i in range (4):
    hc.forward(100)
    hc.right(90)
hc.end_fill()
hc.color("#FFBB00")
hc.begin_fill()
hc.penup()
hc.goto(-140,90)
hc.pendown()

for i in range (4):
    hc.forward(100)
    hc.right(90)
hc.end_fill()
hc.color("#00A1F1")
hc.begin_fill()
hc.penup()
hc.goto(-250,90)
hc.pendown()

for i in range (4):
    hc.forward(100)
    hc.right(90)
hc.end_fill()
hc.pencolor("black")
hc.penup()
hc.goto(-20,50)
hc.pendown()
hc.pensize(12)
hc.write("Microsoft",font=("calbri",50,"bold"))

hc.hideturtle()

turtle.done()