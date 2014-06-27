__author__ = 'Vincent'


from kivy.uix.widget import Widget
import random
from kivy.graphics import Rectangle, Color
from kivy.uix.image import Image


class Stone():
    def __init__(self, x, y, speed, traject, size):
        self.block_size = size
        self.x = x
        self.y = y
        self.traject = traject
        self.speed = random.randint(1, int(speed) + 1)
        color = (random.randint(0, 255), 1, 1)
        Color(*color, mode="hsv")

        if self.block_size > 25 and self.block_size < 50:
            source_url = "artwork/50_Stone.png"
        elif self.block_size > 50 and self.block_size < 75:
            source_url = "artwork/75_Stone.png"
        elif self.block_size > 75:
            source_url = "artwork/Stone_125.png"
        else:
            source_url = "artwork/25_Stone.png"

        self.rect = Image(pos=(self.x, self.y), size=(self.block_size, self.block_size), source=source_url)

    def draw(self):
        self.rect.pos = (self.x, self.y)

    def fall(self):
        if self.traject == 1:
            self.y = self.y - self.speed
        elif self.traject == 2:
            self.y = self.y - self.speed
            self.x = self.x - self.speed / 2
        elif self.traject == 3:
            self.y = self.y - self.speed
            self.x = self.x + self.speed / 2
        elif self.traject == 4:
            self.y = self.y - self.speed
            self.x = self.x - self.speed / 4
        elif self.traject == 5:
            self.y = self.y - self.speed
            self.x = self.x + self.speed / 4
        else:
            self.y = self.y - self.speed

    def getY(self):
        return self.y

    def collision(self, player):
         if player.x <= (self.x + self.block_size) and self.x <= (player.x + 5) and 25 <= (self.y + self.block_size) and self.y <= self.block_size:
             return True

    def getRect(self):
        self.rect

    def getSize(self):
        return self.block_size

    def outOfScreen(self):
        self.y -= 1000
        self.x -= 1000

    def getCoord(self):
        return "y: " + str(self.y) + " x: " + str(self.x) + " size: " + str(self.block_size)
