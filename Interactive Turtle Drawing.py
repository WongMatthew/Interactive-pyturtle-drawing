# Interactive Turtle Drawing
# Matthew Wong
# 10/18/2020
# Draws different patterns for the user, user can give inputs to change size of patterns

import turtle
# Initialize Turtle
drawing = turtle.Turtle()
# Initialize screen
screen = turtle.Screen()
# Set turtle speed
drawing.speed(0)

# PatternA - spiral
def PatternA(length): 
  while length>0:
    drawing.forward(length)
    drawing.right(1.01 * 360/3)
    length = length - 10
    
# PatternB - square made w/ recurssion
def PatternB(sz):
  for i in range(sz):
    if i > sz-(sz/7):
      drawing.color("orange")
      drawing.forward(i)
    elif i > sz-(sz/6):
      drawing.color("yellow")
      drawing.forward(i)
    elif i > sz-(sz/5): 
      drawing.color("pink")
      drawing.forward(i)
    elif i > sz-(sz/4):
      drawing.color("magenta")
      drawing.forward(i)
    elif i > sz-(sz/3):
      drawing.color("purple")
      drawing.forward(i)
    elif i > sz-(sz/2):
      drawing.color("blue")
      drawing.forward(i)
    else:
      drawing.color("violet")
      drawing.forward(i)
    drawing.right(270)

# PatternC - star made w/ recurssion
def PatternC():
  for i in range(800):
    if i > 650:
      drawing.color("orange")
      drawing.forward(i)
    elif i > 550:
      drawing.color("red")
      drawing.forward(i)
    elif i > 450:
      drawing.color("blue")
      drawing.forward(i)
    elif i > 350:
      drawing.color("purple")
      drawing.forward(i)
    elif i > 250:
      drawing.color("magenta")
      drawing.forward(i)
    else:
      drawing.color("pink")
      drawing.forward(i)
    drawing.right(169)    

# Introduce user to list of commands
print("For PatternA, enter 'PatA'. For PatternB, enter 'PatB'. For PatternC, enter 'PatC'. To clear the screen, enter 'Clear'. To exit, enter 'Exit'")

while True:
  question = input().strip("!.,?").lower()
  if question == "pata":
# Only accept int values >= 350 for lgnth for PatternA
    while True:
      try:
        lgnth = int(input("How big would you like the drawing to be? Size must be greater than or equal to 350: "))
        if lgnth >= 350:
          break
        else:
          print("Thats not a valid number")
      except:
        print("Thats not a valid number")
    PatternA(lgnth)
  elif question == "patb":
# Only accept int values >= 50 for size for PatternB
    while True:
      try:
        size = int(input("How big would you like the drawing to be? Size must be greater than or equal to 50: "))
        if size >= 50:
          break
        else:
          print("Thats not a valid number")
      except:
        print("Thats not a valid number")
    PatternB(size)
  elif question == "patc":
    PatternC()
# Resets the turtle position + screen
  elif question == "clear":
    drawing.clear()
    drawing.penup()
    drawing.goto(0,0)
    drawing.pendown()
# Clears screen and exits the bot; ends the loop
  elif question == "exit":
    drawing.clear()
    print("Goodbye")
    break
  else:
    print("I dont know what that means")
  
screen.exitonclick()
