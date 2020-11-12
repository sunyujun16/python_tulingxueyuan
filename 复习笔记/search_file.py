import os


def search_file(start_path, filename):

    os.chdir(start_path)
    file_list = os.listdir(os.curdir)

    for file in file_list:

        if file == filename:
            full_name = "path:{}".format(os.getcwd() + '/' + file)
            print(full_name)

        if os.path.isdir(file):
            search_file(file, filename)
            os.chdir(os.pardir)


search_file('/home/sun/tulingxueyuan/复习笔记/111', 'gohome.txt')