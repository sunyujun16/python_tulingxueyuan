import random
import tkinter
import settings


class Enemy():
    def __init__(self, canvas):
        self.canvas = canvas
        self.pos = [random.randint(10, 530), random.randint(60, 300)]
        self.width = settings.enemy_width
        self.height = settings.enemy_height
        self.surface = None
        self.direction = [random.randint(-1, 1), 1]
        self.img = tkinter.PhotoImage(file=settings.img_path + settings.filename_enemy + settings.suffix)

    def draw_enemy(self):
        self.surface = self.canvas.create_image(self.pos[0], self.pos[1], image=self.img, anchor=tkinter.SW, tag='enemy')

    def move_enemy(self):
        self.canvas.move(self.surface, self.direction[0] * settings.enemy_step, self.direction[1] * settings.enemy_step)
        self.pos[0] += self.direction[0] * settings.enemy_step
        self.pos[1] += self.direction[1] * settings.enemy_step

    def get_coordinates(self):
        self.nw = [self.pos[0], self.pos[1] - self.height]
        self.se = [self.pos[0] + self.width, self.pos[1]]
        self.sw = [self.pos[0], self.pos[1]]
        self.ne = [self.pos[0] + self.width, self.pos[1] - self.height]

    def delete_enemy(self):
        pass

    def check_out_range(self):
        self.get_coordinates()
        if self.nw[0] <=0:
            self.direction[0] *= -1
        if self.ne[0] >= settings.screen_width:
            self.direction[0] *= -1

    def is_hit_bottom(self):
        if self.sw[1] >= settings.screen_height:
            return True


