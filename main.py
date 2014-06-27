from kivy.app import App
from kivy.graphics import Color
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.clock import Clock
from Ruby import Ruby
from Stone import Stone
from Player import Player
from Properties import Properties
from Score import Score
from kivy.uix.screenmanager import Screen
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder

import random

Builder.load_string("""
<StartGame>:
    id: game_starter
    BoxLayout:
        orientation: 'vertical'
        Label:
            text: "Minecollapse"
            font_size: 82
        Button:
            text: "Start"
            on_touch_up: game_starter.start_game()

<Game>:
    canvas:

<ScoreScreen>:
    id: score_screen
    BoxLayout:
        orientation: 'vertical'
        Label:
            text: 'Score: '
            font_size: 32
        Label:
            text: 'Game Over'
            font_size: 82
        Button:
            text: 'Restart'
            on_touch_up: score_screen.start_game()
        Button:
            text: 'watch highscores'
            on_touch_up: root.manager.current = 'highscore'

<HighscoreScreen>:
    BoxLayout:
        orientation: 'vertical'
        Label:
            text: 'Them highscores'


""")

root = ScreenManager()

class StartGame(Screen):
    def start_game(self):
        root.current = 'game'
        game.start()



class ScoreScreen(Screen):
    def start_game(self):
        root.current = 'game'
        game.start()

class HighscoreScreen(Screen):
    pass


class Game(Screen):
    started = False


    def start(self):
        if self.started == False:
            self.init_objects()
            Clock.schedule_interval(self.update, 0.015)
            self.started = True

    def init_objects(self):
        with self.canvas:
            self.stones = []
            self.rubies = []
            self.player = Player(self.width / 2)
            self.properties = Properties()
            self.score = Score(self.height)


    def on_touch_down(self, touch):
        self.firstx = touch.x
        if self.started:
            if touch.x > (self.width / 2):
                self.player.move_right()
            else:
                self.player.move_left()

    def on_touch_up(self, touch):
        if self.started:
            if touch.x > (self.width / 2):
                self.player.stop_move_right()
            else:
                self.player.stop_move_left()

    def update(self, dt):
        self.properties.MAX_SPEED += 0.001
        if not self.properties.BLOCK_FREQ == 1:
            self.properties.BLOCK_FREQ -= 0.00005
        self.properties.MAX_SIZE += 0.02

        #score
        self.score.count_score()

        self.player.movement(self.width - 22)

        with self.canvas:
            #STONES
            if random.randint(0, int(self.properties.BLOCK_FREQ)) == 5:
                self.stones.append(
                    Stone(
                        random.randint(0, self.width),
                        1000,
                        self.properties.MAX_SPEED,
                        random.randint(0, 6),
                        random.randint(10, int(self.properties.MAX_SIZE))
                    )
                )


            for stone in self.stones:
                stone.draw()
                if stone.collision(self.player):
                    self.end_game()
                stone.fall()

                if stone.getY() < -int(stone.getSize() + 15):
                    self.stones.remove(stone)

            #END STONES

            #RUBIES

            if random.randint(0, 400) == 5:
                self.rubies.append(
                    Ruby(
                        random.randint(0, self.width),
                        1000,
                        self.properties
                    )
                )
            for ruby in self.rubies:
                ruby.draw()
                if ruby.collision(self.player):
                    ruby.outOfScreen()
                    ruby.draw()
                    ruby.dice_option(self.stones)
                ruby.fall()

                if ruby.getY() < -(40):
                    self.rubies.remove(ruby)
            #END RUBIES

            self.player.draw()

    def end_game(self):
        Clock.unschedule(self.update)

        self.canvas.clear()
        self.started = False
        self.properties.reset()

        root.current = "score"

highscores = HighscoreScreen(name="highscore")
scores = ScoreScreen(name="score")
game = Game(name="game")
startgame = StartGame(name="startgame")


class MinecollapseApp(App):
    def build(self):
        root.add_widget(startgame)
        root.add_widget(game)
        root.add_widget(highscores)
        root.add_widget(scores)

        return root


if __name__ == '__main__':
    MinecollapseApp().run()
