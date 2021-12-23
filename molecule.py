from turtle import Turtle
import random


class Molecule(Turtle):

    def __init__(self, board_w, board_h, speed):
        super().__init__()
        self.shape("circle")
        self.color("yellow")
        self.size_a = 0.5
        self.size_b = 0.5
        self.shapesize(self.size_a, self.size_b)
        self.penup()
        self.board_w = board_w
        self.board_h = board_h
        self.speed = speed
        x = random.randint(-0.95*board_w/2, 0.95*board_w/2)
        y = random.randint(-0.95*board_h/2, 0.95*board_h/2)
        self.goto(x, y)
        self.direction = random.randint(0, 360)
        self.setheading(self.direction)

    def move(self, m_mode):
        if m_mode == 0:
            self.direction = random.randint(0, 360)
            self.setheading(self.direction)
        self.forward(self.speed)

    def bounce(self, b_mode, m_mode):
        if b_mode == 0:     # bez granic
            pass
        elif b_mode == 1:     # normalne granice
            if m_mode == 0: # przypadek chaotic move
                if self.xcor() < -400:
                    self.goto(-400, self.ycor())
                elif self.xcor() > 400:
                    self.goto(400, self.ycor())
                elif self.ycor() < -400:
                    self.goto(self.xcor(), -400)
                elif self.ycor() > 400:
                    self.goto(self.xcor(), 400)
                self.speed = -self.speed
            if m_mode == 1:               # przypadek straight move
                angle = self.heading()

                if self.ycor() > 400 or self.ycor() < -400:
                    if 0 < angle < 180:
                        self.setheading(0 - angle)
                    else:
                        self.setheading(360 - angle)

                elif self.xcor() > 400 or self.xcor() < -400:

                    if 0 < angle < 180:
                        self.setheading(180 - angle)
                    else:
                        self.setheading(540 - angle)

        elif b_mode == 2:       # wirtualne granice
            x = random.randint(-0.95 * self.board_w / 2, 0.95 * self.board_w / 2)
            y = random.randint(-0.95 * self.board_h / 2, 0.95 * self.board_h / 2)
            self.goto(x, y)

    def size_increase(self, r1, r2):

        rx = (r1 ** 3 + r2 ** 3) ** 0.333
        self.size_a = rx
        self.size_b = rx
        self.shapesize(self.size_a, self.size_b)
        self.color("red")