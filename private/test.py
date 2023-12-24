import turtle

def draw_santa():
    turtle.penup()
    turtle.goto(0, -50)  # Adjusted coordinates for a centered face
    turtle.pendown()
    turtle.color("red")
    turtle.begin_fill()
    turtle.circle(70)  # Increased the radius for a larger face
    turtle.end_fill()

    # Draw Santa's eyes
    turtle.penup()
    turtle.goto(-20, 20)
    turtle.pendown()
    turtle.color("black")
    turtle.begin_fill()
    turtle.circle(15)
    turtle.end_fill()

    turtle.penup()
    turtle.goto(20, 20)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(15)
    turtle.end_fill()

    # Draw Santa's nose
    turtle.penup()
    turtle.goto(0, 10)
    turtle.pendown()
    turtle.color("orange")
    turtle.begin_fill()
    turtle.circle(5)
    turtle.end_fill()
    
      # Draw the triangle (Santa's beard)
    turtle.penup()
    turtle.goto(-15, -50)
    turtle.pendown()
    turtle.color("Orange")
    turtle.begin_fill()
    for _ in range(3):
        turtle.forward(30)
        turtle.left(120)
        # turtle.forward(30)
    turtle.end_fill()

# # Example usage:
turtle.speed(18)
draw_santa()
turtle.done()
