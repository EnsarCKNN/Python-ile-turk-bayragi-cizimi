import turtle

t = turtle.Turtle()
w = turtle.Screen()
w.title("Türk Bayrağı")
w.setup(width=720,height=420)
w.bgcolor("red")

t.up()
t.goto(-100,-100)
t.color('white')
t.begin_fill()
t.circle(120)
t.end_fill()
 
t.goto(-70,-80)
t.color('red')
t.begin_fill()
t.circle(100)
t.end_fill()

t.goto(0,35)
t.fillcolor("white")
t.begin_fill()
 
for i in range(5):
    t.forward(150)
    t.right(144)
t.end_fill()
 
t.goto(-130,-190)
t.color("white")
t.write("@EnsarCKNN", font=("Verdana", 17,"bold"))
 
t.goto(-999,-0)
 
w.exitonclick()