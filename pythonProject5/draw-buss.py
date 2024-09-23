import turtle


screen = turtle.Screen()
screen.title("رسم شكل باستخدام Turtle")

t = turtle.Turtle()
t.shape("turtle")
t.speed(1)


for _ in range(4):
 t.forward(100)
 t.right(90)

turtle.done()