import threading
import time

movie_list = ["Leon.mkv", "ForestGump.avi", "Devil.mp4", "nothing.rmvb"]
music_list = ["Adele.mp3", "Taylor.mp3"]

movie_format = ['mkv', 'avi', 'mp4']
music_format = ['mp3', 'ape']


def play(items):
    for item in items:
        if item.split(".")[1] in movie_format:
            print("开始播放视频%s" % item, time.ctime())
            time.sleep(1)
        elif item.split(".")[1] in music_format:
            print("开始播放音乐%s" % item)
            time.sleep(1)
        else:
            print("不能播放%s文件" % item)
            time.sleep(1)


class Play(threading.Thread):
    def __init__(self, play_list):  # 妈的,少写个下划线居然没有提示,草他奶奶的
        threading.Thread.__init__(self)
        self.play_list = play_list

    def run(self):
        play(self.play_list)


p1 = Play(movie_list)
p2 = Play(music_list)

p1.start()
p2.start()

