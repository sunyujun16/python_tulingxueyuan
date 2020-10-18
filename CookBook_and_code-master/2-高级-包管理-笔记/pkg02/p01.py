print("我是他娘的p01")

class Student(object):
    def __init__(self, age=0, name="Nothing"):
        self.age = age
        self.name = name

    def say(self):
        print("My name is {0}, {1} years old".format(self.name, self.age))


def say_hello():
    print("欢迎来到图灵学员")
