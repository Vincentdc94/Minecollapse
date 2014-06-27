__author__ = 'Vincent'

from kivy.graphics import Color
from kivy.uix.image import Image

class Player():

    def __init__(self, width):
        self.x = width
        self.speed = 5
        self.width = 15
        self.height = 35
        self.movements = []
        color = (255, 1, 1)
        Color(*color)
        self.rect = Image(pos=(self.x, 0), size=(self.width, self.height), source="artwork/Miner_unfinished.png")

    def draw(self):
        self.rect.pos = (self.x, 0)


    def move_right(self):
        self.movements.append("right")
        if "left" in self.movements:
            self.movements.remove("left")

    def move_left(self):
       self.movements.append("left")
       if "right" in self.movements:
           self.movements.remove("right")

    def stop_move_right(self):
        if "right" in self.movements:
            self.movements.remove("right")

    def stop_move_left(self):
        if "left" in self.movements:
            self.movements.remove("left")

    def movement(self, screenwidth):
        if "left" in self.movements:
            if not self.x < 10:
                self.x -= 10
        elif "right" in self.movements:
            if not self.x > screenwidth:
                self.x += 10
