# ClickSmileKaleidoscope.py
# Billy Ridgeway
# Creates a kaleidoscope of smilies reflected across the x axis.

import random               # Imports the random library.
import turtle               # Imports turtle library.
t = turtle.Pen()            # Creates a new turtle pen called t.
t.speed(0)                  # Sets the speed of the pen to fast.
t.hideturtle()              # Hides the pen.
turtle.bgcolor("black")     # Sets the background color to black.
angle = t.heading()         # Keeps track of the pen's direction.


# Defines our kaleidoscopt function using spirals
def draw_kaleido(x,y):
    draw_smileyUp(x,y)      # Calls the draw smiley up function.
    draw_smileyUp(-x,y)     # Calls the draw smiley up function.
    draw_smileyD(-x,-y)     # Calls the draw smiley upside down function.
    draw_smileyD(x,-y)      # Calls the draw smiley upside down function.

def draw_smileyUp(x, y):    # Defines a function to draw a right side up smiley.
    t.penup()
    t.setpos(x, y)
    t.pendown()

    # Head
    t.pencolor("yellow")
    t.fillcolor("yellow")
    t.begin_fill()
    t.circle(50)
    t.end_fill()

    # Left eye
    t.setpos(x-15, y+60)
    t.fillcolor("blue")
    t.begin_fill()
    t.circle(10)
    t.end_fill()

    # Right eye
    t.setpos(x+15, y+60)
    t.begin_fill()
    t.circle(10)
    t.end_fill()

    # Mouth
    t.setpos(x-25, y+40)
    t.pencolor("black")
    t.width(10)
    t.goto(x-10, y+20)
    t.goto(x+10, y+20)
    t.goto(x+25, y+40)
    t.width(1)

def draw_smileyD(x, y):     # Defines a function to draw an upside down smiley.
    t.penup()
    t.setpos(x, y)
    t.pendown()

    # Head
    t.pencolor("yellow")
    t.fillcolor("yellow")
    t.begin_fill()
    t.circle(50)
    t.end_fill()

    # Left eye
    t.setpos(x-15, y+30)
    t.fillcolor("blue")
    t.begin_fill()
    t.circle(10)
    t.end_fill()

    # Right eye
    t.setpos(x+15, y+30)
    t.begin_fill()
    t.circle(10)
    t.end_fill()

    # Mouth
    t.setpos(x-25, y+60)
    t.pencolor("black")
    t.width(10)
    t.goto(x-10, y+80)
    t.goto(x+10, y+80)
    t.goto(x+25, y+60)
    t.width(1)

turtle.onscreenclick(draw_kaleido) # Calls the draw kaleido function.
        
    


            
