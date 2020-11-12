import asyncio
import time

movie_list = ["Leon.mkv", "ForestGump.avi", "Devil.mp4", "nothing.rmvb"]
music_list = ["Adele.mp3", "Taylor.mp3"]

movie_format = ['mkv', 'avi', 'mp4']
music_format = ['mp3', 'ape']


async def play(items):
    for item in items:
        if item.split(".")[1] in movie_format:
            print("开始播放视频%s" % item, time.ctime())
            await asyncio.sleep(1)
        elif item.split(".")[1] in music_format:
            print("开始播放音乐%s" % item, time.ctime())
            await asyncio.sleep(1)
        else:
            print("不能播放%s文件" % item, time.ctime())
            await asyncio.sleep(1)


if __name__ == '__main__':
    tasks = []
    tasks.append(play(movie_list))
    tasks.append(play(music_list))

    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()



