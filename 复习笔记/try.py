import json


def check_file(json_):
    with open(json_, 'r+') as js:
        ex_date = json.load(js)
        ex_date = js.read()
        print(ex_date)


check_file('/home/sun/tulingxueyuan/复习笔记/1234.json')