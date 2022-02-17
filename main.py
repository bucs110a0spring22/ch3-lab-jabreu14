import turtle               #1. import modules
import random

#Part A
window = turtle.Screen()       # 2.  Create a screen
window.bgcolor('lightblue')

michelangelo = turtle.Turtle()    # 3.  Create two turtles
leonardo = turtle.Turtle()
michelangelo.color('orange')
leonardo.color('blue')
michelangelo.shape('turtle')
leonardo.shape('turtle')

michelangelo.up()          # 4.  Pick up the pen so we don’t get lines
leonardo.up()
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

## 5. your code goes here
michelangelo.forward(random.randrange(1,100)) 
leonardo.forward(random.randrange(1,100))
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)
for i in range(10):
  michelangelo.forward(random.randrange(1,10))
  leonardo.forward(random.randrange(1,10))
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)
# Part B - complete part B here
michelangelo.down()
#Triangle
for i in range(3):
  michelangelo.forward(30)
  michelangelo.left(360/3)
michelangelo.clear()
#Square
for i in range(4):
  michelangelo.forward(30)
  michelangelo.left(360/4)
michelangelo.clear()
#Hexagon
for i in range(6):
  michelangelo.forward(30)
  michelangelo.left(360/6)
michelangelo.clear()
#Nonagon
for i in range(9):
  michelangelo.forward(30)
  michelangelo.left(360/9)
michelangelo.clear()
#Dodecagon
for i in range(12):
  michelangelo.forward(30)
  michelangelo.left(360/12)
michelangelo.clear()



window.exitonclick()
