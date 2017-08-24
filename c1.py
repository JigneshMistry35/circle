import turtle
my_turtle=turtle.Turtle()

def square(l,a):
    for i in range(4):
        my_turtle.forward(l)
        my_turtle.right(a)

    my_turtle.right(15)
square(100,90)

for i in range(20):
    square(100,90)
