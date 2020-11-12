import tkinter
import settings


class Hero(object):
    def __init__(self, canvas):
        self.pos = settings.hero_original_pos
        self.width = settings.hero_width
        self.height = settings.hero_height
        self.step = settings.hero_step
        self.lives = settings.hero_lives
        self.score = settings.hero_score
        self.canvas = canvas
        self.surface = None
        self.direction = [0, 0]

        # 这里如果不用canvas, 而是用root来绑定的话, 就不用bind_all了, 只用bind🕘就行, 我猜的.
        self.canvas.bind_all('<Key-Up>', self.key_pressed)
        self.canvas.bind_all('<Key-Down>', self.key_pressed)
        self.canvas.bind_all('<Key-Left>', self.key_pressed)
        self.canvas.bind_all('<Key-Right>', self.key_pressed)

        self.img_num = 0

    def draw_hero(self):
        # establish surfaces of heroes for moving them
        filename_hero = settings.get_filename_hero()
        self.img = tkinter.PhotoImage(file=settings.img_path + filename_hero + settings.suffix)
        self.surface = self.canvas.create_image(self.pos[0], self.pos[1], anchor=tkinter.SW, image=self.img,
                                                tag='hero')

    def key_pressed(self, event):
        # 根据按键event修改direction. 这里不要上下移动的功能了, 鸡肋
        # if event.keysym == 'Up' and self.direction[1] >= 0:
        #     self.direction[1] -= 1
        # if event.keysym == 'Down' and self.direction[1] <= 0:
        #     self.direction[1] += 1
        if event.keysym == 'Left' and self.direction[0] >= 0:
            self.direction[0] -= 1
        if event.keysym == 'Right' and self.direction[0] <= 0:
            self.direction[0] += 1

    def move_hero(self):
        # 根据direction进行移动
        self.canvas.move(self.surface, self.direction[0]*settings.hero_step, self.direction[1]*settings.hero_step)
        self.pos[0] += self.direction[0]*settings.hero_step
        self.pos[1] += self.direction[1]*settings.hero_step

    def get_coordinates(self):
        self.nw = [self.pos[0], self.pos[1]-self.height]
        self.se = [self.pos[0]+self.width, self.pos[1]]
        self.sw = [self.pos[0], self.pos[1]]
        self.ne = [self.pos[0]+self.width, self.pos[1]-self.height]

    def when_out_range(self):
        self.get_coordinates()
        if self.nw[0] <= 0:
            self.direction[0] = 0
        if self.ne[0] >= settings.screen_width:
            self.direction[0] = 0
