import turtle
import math
 
def fiboPlot(n):
    a = 0
    b = 1
    square_a = a
    square_b = b

    x.pencolor("white")
 
    x.forward(b * factor)
    x.left(90)
    x.forward(b * factor)
    x.left(90)
    x.forward(b * factor)
    x.left(90)
    x.forward(b * factor)
 
    temp = square_b
    square_b = square_b + square_a
    square_a = temp
     
    for i in range(1, n):
        x.backward(square_a * factor)
        x.right(90)
        x.forward(square_b * factor)
        x.left(90)
        x.forward(square_b * factor)
        x.left(90)
        x.forward(square_b * factor)
 
        temp = square_b
        square_b = square_b + square_a
        square_a = temp
 
    x.penup()
    x.setposition(factor, 0)
    x.seth(0)
    x.pendown()
 
    x.pencolor("white")
 
    x.left(90)
    for i in range(n):
        print(b)
        fdwd = math.pi * b * factor / 2
        fdwd /= 90
        for j in range(90):
            x.forward(fdwd)
            x.left(1)
        temp = a
        a = b
        b = temp + b

factor = 1

n = int(input('Für wie viele Elemente der Fibonacci Sequenz soll die Spirale gezeichnet werden? '))

if n > 0:
    print("Fibonacci sequenz für", n, "Elemente:")
    x = turtle.Turtle()
    turtle.bgcolor("black")
    x.speed(100)
    fiboPlot(n)
    turtle.done()
else:
    print("i > 0")