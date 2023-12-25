import turtle

def draw_santa():
    # turtle.penup()
    # turtle.goto(0, -90)  # Adjusted coordinates for a centered face
    # turtle.pendown()
    # turtle.color("red")
    # turtle.begin_fill()
    # turtle.circle(70)  # Increased the radius for a larger face
    # turtle.end_fill()

    # # Draw Santa's eyes
    # turtle.penup()
    # turtle.goto(-20, 20)
    # turtle.pendown()
    # turtle.color("black")
    # turtle.begin_fill()
    # turtle.circle(15)
    # turtle.end_fill()

    # turtle.penup()
    # turtle.goto(20, 20)
    # turtle.pendown()
    # turtle.begin_fill()
    # turtle.circle(15)
    # turtle.end_fill()

    # # Draw Santa's nose
    # turtle.penup()
    # turtle.goto(0, 10)
    # turtle.pendown()
    # turtle.color("orange")
    # turtle.begin_fill()
    # turtle.circle(5)
    # turtle.end_fill()
    
    #   # Draw the triangle (Santa's beard)
    # turtle.penup()
    # turtle.goto(-15, -50)
    # turtle.pendown()
    # turtle.color("orange")
    # turtle.begin_fill()
    # for _ in range(3):
    #     turtle.forward(30)
    #     turtle.left(120)
    #     # turtle.forward(30)
    # turtle.end_fill()
    
    
    
    # # Draw Santa's face
    turtle.penup()
    turtle.goto(0, -260)  # Adjusted coordinates for a centered face
    turtle.pendown()
    turtle.color("red")
    turtle.begin_fill()
    turtle.circle(60)  # Adjusted the radius for a more proportional face
    # turtle.end_fill()

    # # Draw Santa's eyes
    # turtle.penup()
    turtle.goto(-25, -180)
    # turtle.pendown()
    # turtle.color("black")
    # turtle.begin_fill()
    # turtle.circle(10)  # Adjusted the radius of the eyes
    # turtle.end_fill()

    # turtle.penup()
    # turtle.goto(20, 20)
    # turtle.pendown()
    # turtle.begin_fill()
    # turtle.circle(10)  # Adjusted the radius of the eyes
    # turtle.end_fill()

    # # Draw Santa's nose
    # turtle.penup()
    # turtle.goto(0, 0)  # Adjusted the nose position
    # turtle.pendown()
    # turtle.color("orange")
    # turtle.begin_fill()
    # turtle.circle(7)  # Adjusted the radius of the nose
    # turtle.end_fill()

    # # Draw Santa's mouth
    # turtle.penup()
    # turtle.goto(-15, -15)
    # turtle.pendown()
    # turtle.color("black")
    # turtle.width(5)
    # turtle.right(90)
    # turtle.circle(15, 180)  # Draw a semi-circle for the mouth
    # turtle.width(1)

# # Example usage:
turtle.speed(4)
draw_santa()
turtle.done()
