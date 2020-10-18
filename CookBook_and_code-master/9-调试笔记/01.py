

def say_hello(name):
    print("I want to say hello with your, {0}".format(name))
    print("Hello, {0}".format(name))
    print("Done...............")


if __name__ == "__main__":
    print('***' * 10)
    name = input("Please input your name: ")
    print(say_hello(name=name))
    print('@@@' * 10)
    # 测试案例
