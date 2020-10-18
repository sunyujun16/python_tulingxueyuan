
# 包含学生类、
# 一个say_hello函数
# 一个打印语句


class Student(object):
    def __init__(self, age=0, name="Nothing"):
        self.age = age
        self.name = name

    def say(self):
        print("My name is {0}, {1} years old".format(self.name, self.age))


def say_hello():
    print("欢迎来到图灵学员")


# 此判断语句建议一直作为程序的入口
if __name__ == '__main__':
    print("抢钱抢踉跄娘们p01")  # 这种代码最好不要有, 导入时会被执行.
