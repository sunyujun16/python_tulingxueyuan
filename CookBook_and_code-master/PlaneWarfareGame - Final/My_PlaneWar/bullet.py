import tkinter
import settings


class Bullet():
    def __init__(self, hero, canvas):
        self.canvas = canvas
        hero.get_coordinates()
        self.pos = [hero.nw[0]+hero.width/2, hero.nw[1]]
        self.width = settings.bullet_width
        self.height = settings.bullet_height
        self.surface = None
        self.direction = [0, -1]
        self.img = tkinter.PhotoImage(file=settings.img_path + settings.filename_bullet + settings.suffix)
        self.bullet_hit = False
        
    def draw_bullet(self):
        self.surface = self.canvas.create_image(self.pos[0], self.pos[1], image=self.img, anchor=tkinter.SW,
                                                tag='bullet')

    def move_bullet(self):
        self.canvas.move(self.surface, self.direction[0], self.direction[1] * settings.bullet_step)
        # self.pos[0] += self.direction[0] * settings.bullet_step
        self.pos[1] += self.direction[1] * settings.bullet_step

    def get_coordinates(self):
        self.nw = [self.pos[0], self.pos[1] - self.height]
        self.se = [self.pos[0] + self.width, self.pos[1]]
        self.sw = [self.pos[0], self.pos[1]]
        self.ne = [self.pos[0] + self.width, self.pos[1] - self.height]

    def is_out_range(self):
        self.get_coordinates()
        if self.nw[1] <= 0:
            return True

