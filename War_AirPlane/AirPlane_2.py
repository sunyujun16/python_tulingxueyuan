# v2: 让小蜜蜂会动，从上往下慢慢飞 // 能控制小蜜蜂左右移动
# 入场算法： y轴负数 // x轴要有一定的富余，保证蜜蜂不会贴边 // 右侧需要更大富余 //
# 移动速度问题，包括x方向和y方向的速度。蜜蜂和英雄两个方向移动，其他元素只有y方向运动
#     英雄飞机移动由上下左右键盘控制
#     速度可以是一个tuple=(x,y)
# 方向问题：
#     具体移动方向由x,y控制
#     值只能是-1,0,1。只表示矢量方向，不表示大小
#     应该是一个tuple，包括(x,y)轴的方向，(0,1)表明向下运动

import tkinter
import time
import random as rd

# 蜜蜂从上向下运动，通过键盘控制左右
# step = 0
direction = (0, 1)

# 本段代码中的x和y代表的其实是步幅，而不是位置坐标
x = 1
y = 1
pos = [50,-50]

def set_right(e):
    global x
    x += 1


def set_left(e):
    global x
    x -= 1


# 创建窗口
root_window = tkinter.Tk()
root_window.title('军仔打飞机')
# root_window.geometry('600x800')

root_window.bind('<Key-Left>', set_left)
root_window.bind('<Key-Right>', set_right)
root_window.resizable(width=False, height=False)

# 创建画布
window_canvas = tkinter.Canvas(root_window, width=480, height=640)
window_canvas.pack()


def main():
    global pos
    global x

    # 创建开始界面
    background_image_fullname = '/home/tlxy/tulingxueyuan/img/background.gif'
    start_img = tkinter.PhotoImage(file=background_image_fullname)
    window_canvas.create_image(480/2, 640/2, anchor=tkinter.CENTER, image=start_img, tags='start')

    # 创建小飞机
    sp_img_name = '/home/tlxy/tulingxueyuan/img/smallplane.gif'
    sp_img = tkinter.PhotoImage(file=sp_img_name)
    window_canvas.create_image(rd.randint(50, 430), -10, anchor=tkinter.CENTER, image=sp_img, tags='sp')

    # 让小飞机动起来
    x *= rd.randint(-1,1)
    # 这里小飞机我没有给坐标的参数，所以没办法控制撞墙之后的反应，下节课见
    ap_move()
    tkinter.mainloop()


def ap_move():
    # global step
    global x
    global y

    # y += 1
    print(x, y)
    window_canvas.move('sp', x, y)

    # step += 1
    window_canvas.after(40, ap_move)

    # # 添加背景图片
    # bg_img_name = "/home/tlxy/tulingxueyuan/img/background.gif"
    # bg_img = tkinter.PhotoImage(file=bg_img_name)
    # # tags的作用是，以后我们使用这个创建好的image可以通过tags调用，相当于起了个外号，贴了个标签
    # window_canvas.create_image(240, 300, anchor=tkinter.CENTER, image=bg_img, tags='bg')

    # # 添加小蜜蜂
    # bee_img_name = "/home/tlxy/tulingxueyuan/img/bee.gif"
    # bee_img = tkinter.PhotoImage(file=bee_img_name)
    # # tags的作用是，以后我们使用这个创建好的image可以通过tags调用，相当于起了个外号，贴了个标签
    # window_canvas.create_image(240, 300, anchor=tkinter.CENTER, image=bee_img, tags='bee')

if __name__ == '__main__':
    main()


# root_window.mainloop()








