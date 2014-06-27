__author__ = 'Vincent'

class Properties():
    BLOCK_FREQ = 10
    MAX_SPEED = 5
    MAX_SIZE = 40

    def reset(self):
        self.BLOCK_FREQ = 10
        self.MAX_SPEED = 5
        self.MAX_SIZE = 40

    def add_speed(self):
        self.MAX_SPEED += 10

    def reduce_speed(self):
        self.MAX_SPEED -= 2