# # 案例:网络IO
# import requests
#
#
# def download_image(url):
#     print("开始下载", url)
#     # 发送网络请求, 下载图片
#     response = requests.get(url)
#     print("搞定")
#     # 图片保存到本地
#     file_name = url.rsplit('_')[-1]
#     with open(file_name, mode='wb') as fb:
#         fb.write(response.content)
#
#
# if __name__ == '__main__':
#     url_list = [
#         'http://wallpaperswide.com/download/silver_satin-wallpaper-1920x1080.jpg',
#         'http://wallpaperswide.com/download/sexy_brunette_3-wallpaper-1920x1080.jpg',
#         'http://wallpaperswide.com/download/red_lipstick-wallpaper-1920x1080.jpg',
#         'http://wallpaperswide.com/download/beautiful_girl_retro_artwork-wallpaper-1920x1080.jpg',
#         'http://wallpaperswide.com/download/kim_ha_yul-wallpaper-1920x1080.jpg'
#     ]
#
#     for item in url_list:
#         download_image(item)
#
