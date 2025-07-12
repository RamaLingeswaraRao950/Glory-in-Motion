import turtle
import math

screen = turtle.Screen()
screen.setup(width=1000, height=700)
screen.title("Modern Waving National Flag of India")
screen.bgcolor("white")

t = turtle.Turtle()
t.speed(0)
t.pensize(2)
t.up()
t.hideturtle()

flag_width = 400
flag_height = 300
stripe_height = flag_height // 3
start_x = -200
start_y = 150


def waving_stripe(color, y_offset):
    t.goto(start_x, start_y - y_offset)
    t.down()
    t.begin_fill()
    t.fillcolor(color)

    for x in range(0, flag_width + 1, 10):
        y = 10 * math.sin(math.radians(x))
        t.goto(start_x + x, start_y - y_offset + y)

    for x in range(flag_width, -1, -10):
        y = 10 * math.sin(math.radians(x))
        t.goto(start_x + x, start_y - y_offset - stripe_height + y)

    t.goto(start_x, start_y - y_offset)
    t.end_fill()
    t.up()


waving_stripe("orange", 0)
waving_stripe("white", stripe_height)
waving_stripe("green", stripe_height * 2)

chakra_radius = 30
chakra_center_x = start_x + flag_width / 2
chakra_center_y = start_y - stripe_height * 1.5

chakra = turtle.Turtle()
chakra.hideturtle()
chakra.speed(0)
chakra.pensize(2)
chakra.color("blue")

chakra.penup()
chakra.goto(chakra_center_x, chakra_center_y - chakra_radius)
chakra.setheading(0)
chakra.pendown()
chakra.circle(chakra_radius)

for i in range(24):
    chakra.penup()
    chakra.goto(chakra_center_x, chakra_center_y)
    chakra.setheading(i * 15)
    chakra.pendown()
    chakra.forward(chakra_radius)

t.goto(start_x - 10, start_y + 10)
t.color("black")
t.setheading(270)
t.pensize(6)
t.down()
t.forward(400)

t.up()
t.goto(-120, -280)
t.color("gray")
t.write("Mera Bharat Mahan - Jai Hind !",
        font=("Times New Roman", 14, "bold"))

star = turtle.Turtle()
star.hideturtle()
star.color("orange")
star.penup()
for i in range(5):
    star.goto(-200 + i * 80, -250)
    star.write("★", font=("Arial", 17, "bold"))
turtle.done()
