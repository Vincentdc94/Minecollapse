__author__ = 'napalm'

from kivy.uix.label import Label
from kivy.graphics import Color
import math


class Score():
    def __init__(self, posy):
        self.score = 0
        color = (255, 1, 1)
        Color(*color)
        self.lbl_score = Label(pos=(45, posy - 100), text="Score")
        self.lbl_score = Label(pos=(45, posy - 150), text=str(math.floor(self.get_score())))

    def count_score(self):
        self.score += 0.12
        self.lbl_score.text = str(math.floor(self.score))

    def get_score(self):
        return self.score




