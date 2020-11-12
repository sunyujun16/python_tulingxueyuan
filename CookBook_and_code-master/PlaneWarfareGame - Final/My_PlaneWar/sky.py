import tkinter
import settings


class Sky():
    def __init__(self, canvas, anchor):
        self.origin_pos = [0, 0]
        self.pos = [self.origin_pos[0], self.origin_pos[1]]
        self.direction = 'Down'
        self.anchor = anchor
        self.canvas = canvas
        self.width = settings.screen_width
        self.height = settings.screen_height
        self.img = tkinter.PhotoImage(file=settings.img_path + settings.filename_sky + settings.suffix)

    def draw_sky(self):
        self.surface = self.canvas.create_image(self.origin_pos[0], self.origin_pos[1], anchor=self.anchor, image=self.img,
                                           tag='sky')

    def move_sky(self):
        # 向下移动, 判断是否出界, 出界就瞬移到起始位置
        if self.pos[1] < self.origin_pos[1] + self.height:
            self.canvas.move(self.surface, 0, 0.5)
            self.pos[1] += 0.5
        else:
            self.canvas.move(self.surface, 0, (-1)*self.height)
            self.pos[1] -= self.height








