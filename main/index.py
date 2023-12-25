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
    # Draw Santa's face
    turtle.penup()
    turtle.goto(170, -150)  # Adjusted coordinates for a centered face
    turtle.pendown()
    turtle.color("red")
    turtle.begin_fill()
    turtle.circle(60)  # Adjusted the radius for a more proportional face
    turtle.end_fill()

    # Draw Santa's eyes
    turtle.penup()
    turtle.goto(150, -165)
    turtle.pendown()
    turtle.color("black")
    turtle.begin_fill()
    turtle.circle(10)  # Adjusted the radius of the eyes
    turtle.end_fill()

    turtle.penup()
    turtle.goto(188, -165)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(10)  # Adjusted the radius of the eyes
    turtle.end_fill()

    # Draw Santa's nose
    turtle.penup()
    turtle.goto(169, -209)
    # Adjusted the nose position
    turtle.right(270)
    turtle.pendown()
    turtle.color("orange")
    turtle.begin_fill()
    for _ in range(6):
        turtle.forward(30)
        turtle.left(120)
        turtle.forward(5)
        turtle.left(120)
    turtle.forward(30)  # Adjusted the radius of the nose
    turtle.end_fill()

    # Draw Santa's mouth
    turtle.penup()
    turtle.goto(190, -165)
    turtle.pendown()
    turtle.color("black")
    turtle.width(5)
    turtle.right(360)
    turtle.circle(15, 180)  # Draw a semi-circle for the mouth
    turtle.width(1)

# Play "Jingle Bell" as background music
def play_music():
    pygame.init()
    pygame.mixer.music.load("jingle_bell.mp3")  # Replace with the path to your music file
    pygame.mixer.music.play(-1)  # -1 means play on loop

# Main function
def main():
    turtle.speed(1)
    turtle.hideturtle()
    
    draw_tree()
    draw_star()
    draw_santa()
    play_music()

    turtle.done()

if __name__ == "__main__":
    main()
