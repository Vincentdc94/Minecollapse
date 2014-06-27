__author__ = 'napalm'

from kivy.graphics import Color
from kivy.uix.image import Image
from Stone import Stone
import random

class Ruby():

    def __init__(self, x, y, props):
        self.x = x
        self.y = y
        self.props = props

        self.rect = Image(pos=(self.x, self.y), size=(40, 32), source="artwork/Ruby.png")

    def dice_option(self, stones):
        choice = random.randint(0, 100)
        if choice == 1:
            self.faster()
            print "faster"
        elif choice < 30:
            self.slower()
            print "slower"
        else:
            print "gone"
            self.clear_screen(stones)

    def faster(self):
        self.props.add_speed()

    def slower(self):
        self.props.reduce_speed()

    def clear_screen(self, stones):
        for stone in stones:
            stone.outOfScreen()
            stone.draw()
            stones.remove(stone)

    def draw(self):
        self.rect.pos = (self.x, self.y)

    def fall(self):
        self.y = self.y - 3


    def outOfScreen(self):
        self.y = self.y - 100
        self.x -= self.y - 100

    def collision(self, player):
         if player.x <= (self.x + 32) and self.x <= (player.x + 5) and 25 <= (self.y + 40) and self.y <= 40:
             return True


    def getY(self):
        return self.y