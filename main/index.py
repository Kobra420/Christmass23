import turtle
import pygame

# Initialize turtle
screen = turtle.Screen()
screen.bgcolor("midnightblue")

# Draw a Christmas tree
def draw_tree():
    turtle.color("green")
    turtle.begin_fill()
    turtle.left(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(90)
    turtle.left(135)
    turtle.forward(90)
    turtle.right(135)
    turtle.forward(28)
    turtle.left(135)
    turtle.forward(73)
    turtle.left(90)
    turtle.forward(73)
    turtle.left(135)
    turtle.forward(40)
    turtle.right(135)
    turtle.forward(90)
    turtle.left(135)
    turtle.forward(80)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(6)
    turtle.end_fill()

# Draw a star
def draw_star():
    turtle.penup()
    turtle.goto(-230, 160)
    turtle.pendown()
    turtle.color("yellow")
    turtle.begin_fill()
    for _ in range(5):
        turtle.forward(110)
        turtle.right(145)
    turtle.end_fill()

# Draw Santa Claus
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

# Play "Jingle Bell" as background music
def play_music():
    pygame.init()
    pygame.mixer.music.load("jingle_bell.mp3")  # Replace with the path to your music file
    pygame.mixer.music.play(-1)  # -1 means play on loop

# Main function
def main():
    turtle.speed(5)
    turtle.hideturtle()
    
    draw_tree()
    draw_star()
    draw_santa()
    play_music()

    turtle.done()

if __name__ == "__main__":
    main()
