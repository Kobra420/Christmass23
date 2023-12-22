import turtle
import pygame

# Initialize turtle
screen = turtle.Screen()
screen.bgcolor("midnightblue")

# Draw a Christmas tree
def draw_tree():
    turtle.color("green")
    turtle.begin_fill()
    turtle.forward(100)
    turtle.left(135)
    turtle.forward(50)
    turtle.right(135)
    turtle.forward(50)
    turtle.left(135)
    turtle.forward(30)
    turtle.right(135)
    turtle.forward(30)
    turtle.left(135)
    turtle.forward(20)
    turtle.right(135)
    turtle.forward(20)
    turtle.left(135)
    turtle.forward(10)
    turtle.right(135)
    turtle.forward(10)
    turtle.end_fill()

# Draw a star
def draw_star():
    turtle.penup()
    turtle.goto(-10, 130)
    turtle.pendown()
    turtle.color("yellow")
    turtle.begin_fill()
    for _ in range(5):
        turtle.forward(25)
        turtle.right(144)
    turtle.end_fill()

# Draw Santa Claus
def draw_santa():
    turtle.penup()
    turtle.goto(-50, -50)
    turtle.pendown()
    turtle.color("red")
    turtle.begin_fill()
    turtle.circle(40)
    turtle.end_fill()

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
