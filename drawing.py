"""My NFT contribution for ENGL 128!"""

from turtle import Turtle, colormode, done

colormode(255)


def main() -> None:
    """The entrypoint for my image."""
    vrinda: Turtle = Turtle()
    x: int = -650
    y: int = 0
    draw_background(vrinda, 255, 240, 230)
    draw_real_woman(vrinda, x, y)
    draw_fake_woman(vrinda, x + 300, y, 3)
    done()

# TODO:
# Add colors to background
# Done!


def draw_background(vrinda: Turtle, r: int, g: int, b: int) -> None:
    """Fills in the background, customized by color."""
    vrinda.speed(100)
    vrinda.penup()
    vrinda.goto(-1000, -1000)
    vrinda.setheading(0.0)
    vrinda.pendown()
    vrinda.pencolor(r, g, b)
    vrinda.fillcolor(r, g, b)
    vrinda.begin_fill()
    i: int = 0
    while i < 4:
        vrinda.forward(2000)
        vrinda.left(90)
        i = i + 1
    vrinda.end_fill()
    vrinda.hideturtle()


def draw_real_woman(vrinda: Turtle, x: int, y: int) -> None:
    vrinda.pencolor(22, 20, 84)
    draw_face(vrinda, x, y)
    draw_half_shoulder(vrinda, x, y)
    draw_neck(vrinda, x, y)
    draw_arm(vrinda, x, y)
    draw_chest(vrinda, x, y)
    draw_hips(vrinda, x, y)
    draw_pelvis(vrinda, x, y)
    return


def draw_fake_woman(vrinda: Turtle, x: int, y: int, count: int) -> None:
    vrinda.pencolor(204, 102, 0)
    if count == 0:
        draw_half_shoulder(vrinda, x, y)
    else:
        draw_shoulders(vrinda, x, y)
    draw_chest(vrinda, x, y)
    draw_hips(vrinda, x, y)
    draw_pelvis(vrinda, x, y)
    if count > 0:
        draw_fake_woman(vrinda, x + 253, y, count - 1)
    return


def draw_half_shoulder(vrinda: Turtle, x: int, y: int) -> None:
    vrinda.speed(100)
    vrinda.pensize(3)
    vrinda.penup()
    vrinda.goto(x, y)
    vrinda.setheading(70)
    vrinda.pendown()
    vrinda.circle(700, 10)
    vrinda.right(180)
    vrinda.circle(30, -40)
    vrinda.circle(30, -40)
    vrinda.setheading(0.0)
    vrinda.forward(30)
    vrinda.penup()
    vrinda.forward(40)
    vrinda.pendown()
    vrinda.forward(30)
    vrinda.setheading(180)
    vrinda.circle(30, -40)
    vrinda.circle(30, -40)
    vrinda.right(180)
    vrinda.circle(400, 10)
    vrinda.forward(30)
    return


def draw_neck(vrinda: Turtle, x: int, y: int) -> None:
    vrinda.speed(100)
    vrinda.penup()  # neck1
    vrinda.goto(x + 91, y + 142)
    vrinda.pendown()
    vrinda.setheading(60)
    vrinda.circle(30, 45)
    vrinda.penup()  # neck2
    vrinda.goto(x + 131, y + 142)
    vrinda.pendown()
    vrinda.setheading(300)
    vrinda.circle(30, -45)

    return


def draw_arm(vrinda: Turtle, x: int, y: int) -> None:
    vrinda.speed(100)
    vrinda.penup()
    vrinda.goto(x + 220, y + 21)
    vrinda.setheading(30)
    vrinda.pendown()
    vrinda.circle(30, 20)
    vrinda.forward(60)
    return


def draw_shoulders(vrinda: Turtle, x: int, y: int) -> None:
    vrinda.speed(100)
    vrinda.pensize(3)
    vrinda.penup()
    vrinda.goto(x, y)
    vrinda.setheading(70)
    vrinda.pendown()
    vrinda.circle(700, 10)
    vrinda.right(180)
    vrinda.circle(30, -40)
    vrinda.circle(30, -40)
    vrinda.setheading(0.0)
    vrinda.forward(30)
    vrinda.penup()
    vrinda.forward(40)
    vrinda.pendown()
    vrinda.forward(30)
    vrinda.setheading(180)
    vrinda.circle(30, -40)
    vrinda.circle(30, -40)
    vrinda.right(180)
    vrinda.circle(400, 10)
    vrinda.forward(30)
    vrinda.circle(200, 10)
    vrinda.setheading(130)
    vrinda.circle(60, -10)
    vrinda.circle(50, -30)
    vrinda.circle(5, -200)
    vrinda.circle(80, -10)
    vrinda.setheading(70)
    vrinda.forward(33)
    return


def draw_chest(vrinda: Turtle, x: int, y: int) -> None:
    vrinda.speed(100)
    vrinda.penup()  # b1
    vrinda.goto(x + 55, y + 100)
    vrinda.pendown()
    vrinda.setheading(270)
    vrinda.circle(50, 40)
    vrinda.circle(10, 30)
    vrinda.circle(10, 30)
    vrinda.setheading(30)
    vrinda.circle(50, 40)
    vrinda.penup()
    vrinda.setheading(0)
    vrinda.forward(20)
    vrinda.pendown()  # b2
    vrinda.setheading(280)
    vrinda.circle(50, 40)
    vrinda.setheading(340)
    vrinda.circle(10, 30)
    vrinda.circle(10, 30)
    vrinda.circle(50, 40)
    draw_dots(vrinda, x, y)
    return


def draw_dots(vrinda: Turtle, x: int, y: int) -> None:
    vrinda.speed(100)
    vrinda.penup()
    vrinda.pensize(2)
    vrinda.setheading(0)
    vrinda.goto(x + 72, y + 80)
    vrinda.pendown()
    vrinda.dot()  # n1
    vrinda.penup()
    vrinda.forward(68)
    vrinda.pendown()
    vrinda.dot()  # n2
    return


def draw_hips(vrinda: Turtle, x: int, y: int) -> None:
    vrinda.speed(100)
    vrinda.penup()  # hip1
    vrinda.pensize(3)
    vrinda.goto(x + 55, y + 70)
    vrinda.pendown()
    vrinda.setheading(110)
    vrinda.circle(100, -50)
    vrinda.setheading(240)
    vrinda.circle(130, 50)
    vrinda.penup()  # hip2
    vrinda.goto(x + 163, y + 70)
    vrinda.pendown()
    vrinda.setheading(250)
    vrinda.circle(100, 50)
    vrinda.setheading(120)
    vrinda.circle(130, -50)
    return


def draw_pelvis(vrinda: Turtle, x: int, y: int) -> None:
    vrinda.speed(100)
    vrinda.penup()  # long line
    vrinda.goto(x + 95, y + -30)
    vrinda.pendown()
    vrinda.setheading(120)
    vrinda.circle(200, -20)
    vrinda.hideturtle()
    vrinda.penup()  # short line
    vrinda.goto(x + 110, y + -60)
    vrinda.pendown()
    vrinda.setheading(243)
    vrinda.circle(200, -10)
    return


def draw_face(vrinda: Turtle, x: int, y: int) -> None:
    vrinda.speed(100)
    vrinda.pensize(3)
    vrinda.penup()
    vrinda.goto(x + 103, y + 220)
    vrinda.pendown()  # eye1
    vrinda.setheading(130)
    vrinda.circle(12, 21)
    vrinda.circle(12, 91)
    vrinda.setheading(300)
    vrinda.circle(12, 91)
    vrinda.circle(12, 21)
    vrinda.goto(x + 104, y + 219)
    vrinda.setheading(160)  # mouth
    vrinda.circle(27, -100)
    vrinda.circle(11, -310)
    vrinda.speed(100)
    vrinda.penup()  # eye2
    vrinda.goto(x + 140, y + 220)
    vrinda.pendown()
    vrinda.setheading(130)
    vrinda.circle(11, 21)
    vrinda.circle(11, 91)
    vrinda.setheading(300)
    vrinda.circle(11, 91)
    vrinda.circle(11, 21)
    vrinda.goto(x + 141, y + 219)
    vrinda.penup()
    vrinda.goto(x + 113, y + 250)  # hair1
    vrinda.pendown()
    vrinda.setheading(120)
    vrinda.circle(23, 90)
    vrinda.circle(30, 50)
    vrinda.forward(50)
    vrinda.circle(20, 80)
    vrinda.penup()
    vrinda.goto(x + 113, y + 250)  # hair2
    vrinda.pendown()
    vrinda.setheading(240)
    vrinda.circle(23, -90)
    vrinda.circle(30, -50)
    vrinda.forward(-50)
    vrinda.circle(20, -80)
    return


if __name__ == "__main__":
    main()
