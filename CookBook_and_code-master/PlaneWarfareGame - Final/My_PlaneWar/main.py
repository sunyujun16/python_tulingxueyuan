import pickle
import time
import tkinter
import settings
from bee import Bee
from bullet import Bullet
from enemies import Enemy
from hero import Hero
from sky import Sky


def create_sky(canvas):
    sky1 = Sky(canvas, tkinter.NW)
    sky2 = Sky(canvas, tkinter.SW)
    sky1.draw_sky()
    sky2.draw_sky()
    return sky1, sky2


def create_hero(canvas):
    hero = Hero(canvas)
    hero.draw_hero()
    return hero


def create_bees(canvas, bee_list):
    for i in range(0, 3):
        bee = Bee(canvas)
        bee.draw_bee()
        bee_list.append(bee)


def add_new_bee(canvas, bee_list):
    bee = Bee(canvas)
    bee.draw_bee()
    bee_list.append(bee)


def create_enemies(canvas, enemy_list):
    for i in range(0, 3):
        enemy = Enemy(canvas)
        enemy.draw_enemy()
        enemy_list.append(enemy)


def add_new_enemy(canvas, enemy_list):
    enemy = Enemy(canvas)
    enemy.draw_enemy()
    enemy_list.append(enemy)


def move_everything(root, canvas, sky1, sky2, hero, bee_list, enemy_list, bullet_list):
    # 以下代码均在规定移动方式, 待重构, move_everything(sky1, sky2, hero, bee_list, enemy_list, bullet_list)
    sky1.move_sky()
    sky2.move_sky()
    hero.move_hero()
    hero.when_out_range()
    # bee/enemy左右出界时反弹
    for bee in bee_list:
        bee.move_bee()
        bee.check_out_range()
    for enemy in enemy_list:
        enemy.move_enemy()
        enemy.check_out_range()
    for bullet in bullet_list:
        bullet.move_bullet()
    pass


def create_bullets(hero, canvas, bullet_list):
    if len(bullet_list) <= settings.bullet_num:
        bullet = Bullet(hero, canvas)
        bullet.draw_bullet()
        bullet_list.append(bullet)
    else:
        pass


def check_hit_bottom(canvas, bullet_list, enemy_list, bee_list, hero):
    for bullet in bullet_list.copy():
        if bullet.is_out_range():
            bullet_list.remove(bullet)
            # 修复最后一颗子弹不能被删除的bug
            if len(bullet_list) == 0:
                canvas.delete('bullet')
    for enemy in enemy_list.copy():
        if enemy.is_hit_bottom():
            enemy_list.remove(enemy)
            add_new_enemy(canvas, enemy_list)
            hero.lives -= 1
    for bee in bee_list.copy():
        if bee.is_hit_bottom():
            bee_list.remove(bee)
            add_new_bee(canvas, bee_list)
            # canvas.delete('bee')
            # 为什么这里不要delete呢, 一方面delete会因为我们的tag设置的太无脑,所以会将list全盘删除. 另一方面,
            # 在下次执行move的时候, 列表中没有的元素会被自动删除, 不过这样在列表为空时会导致最后的元素不能执行move函数, 好在我们
            # 不需要列表为空. 如果需要, 那么还是要用delete, 那么就要在实例化的时候把每个tag区分开来(通过settings.)
            # 也可以参考最后一颗bullet不能删除的bug的代码, 会更简单直接一些.
            hero.lives -= 1


def check_bullet_hit(hero, bullet_list, item_list):
    for bullet in bullet_list.copy():
        bullet.get_coordinates()
        for item in item_list.copy():
            item.get_coordinates()
            if (bullet.nw[0] <= item.se[0] and bullet.ne[0] >= item.sw[0])\
                    and (bullet.nw[1] <= item.sw[1] and bullet.sw[1] >= item.nw[1]):
                bullet_list.remove(bullet)
                item_list.remove(item)
                hero.score += 10
                # 这里删除之后不太方便直接重生一个, 因为传参决定了要调用哪个item函数, 还得另外传参(list)和判断.不如直接写在外部了.
                return True
            else:
                pass


def check_hero_hit(hero, item_list):
    hero.get_coordinates()
    for item in item_list.copy():
        item.get_coordinates()
        if (hero.nw[0] <= item.se[0] and hero.ne[0] >= item.sw[0]) \
                and (hero.nw[1] <= item.sw[1] and hero.sw[1] >= item.nw[1]):
            settings.hero_img_num = 1
            item_list.remove(item)
            hero.lives -= 1
            return True
        else:
            pass


def check_collisions(canvas, hero, bullet_list, bee_list, enemy_list):
    # 判断子弹和敌人们碰撞
    if check_bullet_hit(hero, bullet_list, bee_list):
        add_new_bee(canvas, bee_list)
    if check_bullet_hit(hero, bullet_list, enemy_list):
        add_new_enemy(canvas, enemy_list)
    # 再判断主机和敌人们碰撞
    if check_hero_hit(hero, bee_list):
        add_new_bee(canvas, bee_list)
    if check_hero_hit(hero, enemy_list):
        add_new_enemy(canvas, enemy_list)
    # 前面两个函数把settings.hero_img_num设为1, 下面要实现动画了
    # 那么根据settings.hero_img_num来设定爆炸动画的实现, 先写, 暂不封装.
    # 那么首先我要搞明白: canvas.delete删除的是实例还是仅仅删除了image? 那么既然删除传参是tag, 那么先看tag代表什么, 应该是surface
    # 那就不好办了, 我想删除的是实例呀. 否则hero实例存在, 原来的属性均存在, 变成了一个没图的/透明的hero, 但是所有的属性仍延续
    # 之前的hero, 并且生成新的之后, 属性恐怕要乱套. 那么重新draw, 不就好了吗? 何必要删除实例呢? 只需要hero模块里把导入图片的代码
    # 挪到draw()方法里, 应该就能实现. 实现方法就是逐帧重复"先delete,再draw"的过程, 这样属性不丢失, 完美.
    if settings.hero_img_num == 1 or 1 < settings.hero_img_num <= 39:
        canvas.delete('hero')
        hero.draw_hero()
        settings.hero_img_num += 1
    if settings.hero_img_num == 40:
        settings.hero_img_num = 0
        canvas.delete('hero')
        hero.draw_hero()


def show_stats(canvas, hero):
    canvas.delete('Grade')
    canvas.create_text((5, 5), fill='blue', font=('Helvetica', 20, 'bold'),
                       text='❤:' + str(hero.lives), anchor=tkinter.NW, tag='Grade')

    canvas.delete('score')
    canvas.create_text((595, 5), fill='blue', font=('Helvetica', 20, 'bold'),
                       text='得分:' + str(hero.score), anchor=tkinter.NE, tag='score')


def start_game(root, canvas):

    canvas.delete('start')
    canvas.delete('start_label')
    canvas.delete('gameover')
    canvas.delete('final_score')
    canvas.delete('high_score')
    root.unbind('<Key-space>')

    sky1, sky2 = create_sky(canvas)
    hero = create_hero(canvas)
    # 定义敌人/子弹列表的变量, 然后生成各自的列表. 这定义还费了一番周折, 得总结一下: 如果不先定义, list就变成create_xx()的局部变量了.
    bee_list = []
    enemy_list = []
    bullet_list = []  # 之前把这句放在主循环里面了, 草! 我真是个大傻逼.
    create_bees(canvas, bee_list)
    create_enemies(canvas, enemy_list)
    # 按space触发射击
    root.bind('<Key-space>', lambda shoot: create_bullets(hero, canvas, bullet_list))

    # 主循环 !!!!!!!!!
    while True:
        if settings.game_stats == 'run':

            move_everything(root, canvas, sky1, sky2, hero, bee_list, enemy_list, bullet_list)

            check_hit_bottom(canvas, bullet_list, enemy_list, bee_list, hero)

            check_collisions(canvas, hero, bullet_list, bee_list, enemy_list)

            show_stats(canvas, hero)

            if hero.lives == 0:
                settings.game_stats = 'game_over'

            root.update()

        elif settings.game_stats == 'pause':
            # 创建暂停界面
            pause_img = tkinter.PhotoImage(file=settings.img_path + settings.filename_pause + settings.suffix)
            canvas.create_image(0, 0, anchor=tkinter.NW, image=pause_img, tag='pause')
            root.update()

        elif settings.game_stats == 'quit':
            quit_img = tkinter.PhotoImage(file=settings.img_path + settings.filename_gameover + settings.suffix)
            canvas.create_image(0, 0, anchor=tkinter.NW, image=quit_img, tag='quit')
            canvas.delete('hero')
            canvas.delete('bee')
            canvas.delete('bullet')
            canvas.delete('sky')
            canvas.delete('Grade')
            canvas.delete('enemy')
            with open(r'high_score.txt', 'r') as hs:
                high_score = hs.read()
            hs.close()

            if hero.score >= int(high_score):
                with open(r'high_score.txt', 'w') as hs:
                    hs.write(str(hero.score))
                    canvas.create_text((300, 300), fill='blue', font=('Helvetica', 20, 'bold'),
                                       text='已打破最高记录' + str(hero.score), anchor=tkinter.CENTER, tag='high_score')
                    hero.score = 0
            else:
                canvas.create_text((300, 500), fill='blue', font=('Helvetica', 20, 'bold'),
                                   text='您的得分是' + str(hero.score), anchor=tkinter.CENTER, tag='final_score')

            hs.close()
            root.update()
            time.sleep(1)
            quit()
            break

        elif settings.game_stats == 'game_over':

            canvas.delete('hero')
            canvas.delete('bee')
            canvas.delete('bullet')
            canvas.delete('sky')
            canvas.delete('Grade')
            canvas.delete('enemy')

            gameover_img = tkinter.PhotoImage(file=settings.img_path + settings.filename_gameover + settings.suffix)
            canvas.create_image(0, 0, anchor=tkinter.NW, image=gameover_img, tag='gameover')

            with open(r'high_score.txt', 'r') as hs:
                high_score = hs.read()
            hs.close()

            if hero.score >= int(high_score):
                with open(r'high_score.txt', 'w') as hs:
                    hs.write(str(hero.score))
                    canvas.create_text((300, 300), fill='blue', font=('Helvetica', 20, 'bold'),
                                       text='已打破最高记录' + str(hero.score), anchor=tkinter.CENTER, tag='high_score')
                    hero.score = 0
            else:
                canvas.create_text((300, 500), fill='blue', font=('Helvetica', 20, 'bold'),
                                   text='您的得分是' + str(hero.score), anchor=tkinter.CENTER, tag='final_score')
            hs.close()
            root.update()
            settings.game_stats = 'wait'

        elif settings.game_stats == 'wait':
            root.bind_all('<Key-space>', lambda event: reset_all(root, canvas))
            canvas.create_text((300, 200), fill='blue', font=('Helvetica', 20, 'bold'),
                               text='结束倒计时' + '3', anchor=tkinter.CENTER, tag='3')
            time.sleep(2)
            canvas.delete('3')
            canvas.create_text((300, 200), fill='blue', font=('Helvetica', 20, 'bold'),
                               text='结束倒计时' + '2', anchor=tkinter.CENTER, tag='2')
            time.sleep(2)
            canvas.delete('2')
            canvas.create_text((300, 200), fill='blue', font=('Helvetica', 20, 'bold'),
                               text='结束倒计时' + '1', anchor=tkinter.CENTER, tag='1')
            time.sleep(1)
            quit_game()

        time.sleep(0.017)


def reset_all(root, canvas):
    settings.game_stats = 'run'
    start_game(root, canvas)


def pause():
    settings.game_stats = 'pause'


def restore(canvas):
    try:
        canvas.delete('pause')
    except Exception:
        pass
    settings.game_stats = 'run'


def quit_game():
    settings.game_stats = 'quit'


def main():
    root = tkinter.Tk()
    canvas = tkinter.Canvas(root, width=settings.screen_width, height=settings.screen_height)
    canvas.pack()

    # 创建开始界面
    start_img = tkinter.PhotoImage(file=settings.img_path + settings.filename_start + settings.suffix)
    canvas.create_image(0, 0, anchor=tkinter.NW, image=start_img, tag='start')
    # start_label_img = tkinter.PhotoImage(file=settings.img_path + settings.filename_start_label + settings.suffix)
    # canvas.create_image(0, 0, anchor=tkinter.NW, image=start_label_img, tag='start_label')

    # 绑定按键开始游戏, 源码这里每次按空格都会刷新页面, 不合适, 怎么能让在程序运行时解绑呢...等等! 解绑! unbind
    root.bind('<Key-space>', lambda event: start_game(root, canvas))
    root.bind('<Key-p>', lambda event: pause())
    root.bind('<Key-r>', lambda event: restore(canvas))
    root.bind('<Key-Escape>', lambda event: quit_game())

    tkinter.mainloop()


main()

