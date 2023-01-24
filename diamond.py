import turtle

# Create a turtle object
t = turtle.Turtle()

# Move the turtle to the starting position
t.penup()
t.goto(0,0)
t.pendown()

# Setting the thickness of the line
t.pensize(3)

# loop for rotation
for i in range(360):
    # Loop to draw the diamond shape
    for j in range(4):
        t.color("indigo") #setting color for the first half of the diamond
        t.forward(100)
        t.right(45)
        t.color("violet") #setting color for the second half of the diamond
        t.forward(100)
        t.right(135)
    t.right(120) #rotating the diamond by 1 degree

# Hide the turtle and exit on click
t.hideturtle()
turtle.exitonclick()
