
'''celi() 向上取整
print(math.ceil(0.8))


# floor() 向下取整
# print(math.floor(8.3))


# 查看系统保留的关键词，不能用于变量命名
import keyword
print(keyword.kwlist)


# round() 四舍五入，返回int
print(round(5.84))
print(round(5.12))


# sqrt() 开平方
print(math.sqrt(8))
print(math.sin(90))


# pow() 类似幂运算，计算一个数的乘方，两个参数，第一个是底数，第二个是指数。
print(math.pow(11,2))
# 幂运算，返回int，上面函数返回float
print(4**3)


# fabs() 求绝对值，返回浮点数
print(math.fabs(-3.15))
print(math.fabs(3))


# abs() 求绝对值，非数学模块，而是Python内置的，整数则返回整型，浮点数返回浮点数。
print(abs(3))


# sum是Python内置求和，
# fsum是数学模块中的，对整个序列求和
print(math.fsum([1,4,5,7])) # 返回浮点数
print(sum([1,4,5,7])) #返回原型


# modf()，把数分解为浮点数和整数的元组
print(math.modf(-4.5)) # (-0.5, -4.0)
help(math.modf)


# copysign() 将第二个参数的符号赋予第一个数，并输出第一个数的浮点数
print(math.copysign(3.2,-1))



# random() 获取0-1之间的随机小数，含0不含1
for i in range(10):
    # print(random.random())
    print(random.randint(1,5)) # 随机指定开始和结束值，左右均包含。
'''

'''
# random.randrange() 随机获取指定区间的整数值，可以指定间隔
# for i in range(10):
    # print(random.randrange(-1,-9,-2))

# choice() 随机获取列表中的值
# for i in range(10):
#     print(random.choice([1,4,5,2,145,5,2,5]))

# random.shuffle， 洗牌，打乱顺序，源码已阅，看懂一半

# random.uniform ，随机获取指定范围内的值
# print(random.uniform(0,10))

# 定义类
class Student():
    # 一个空类，pass代表直接跳过
    # pass占位不能省略
    pass

# 定义对象
mingyue = Student()


#
class PythonStudent():
    name = None
    age = 18
    course = 'Python'

    def doHomework(self):
        print('I am doing it.')
        return None

# 实例化
yueyue = PythonStudent()

yueyue.doHomework()
print(yueyue.age)
print(yueyue.name)
# 注意，这里并没有输入参数
'''
'''
输入一个三位数与程序随机数比较大小
1 如果大于程序随机数，则分别输出这三位数的个位，十位，百位
2 如果等于程序随机数，则提示中奖，记100分
3 如果小于程序随机数，则将120个字符输入到文本文件中
（规则是：每一条字符串长度为12，单独占一行，并且前四个是字母，后八个是数字
'''

class MyGame():

    def num_game(self):
        import random
        import math
        score = 0

        while True:
            # 输入函数
            num = input('请输入三位数：')
            # 检测是否是纯数字并且在区间内
            num = int(num)
            if not 100 <= num <= 999 :
                print('请重新输入')
                continue
            else:
                num_p = random.randint(100,999)
                print('随机数为', num_p, '你输入的是', num)

                if num == num_p:
                    print('你中奖了')
                    score += 100
                    print(score)

                if num > num_p:
                    # print('随机数为', num_p, '你输入的是',num)
                    print('个位',num%10,'十位', (num%100)//10,'百位',num//100)

                else:
                    # ascii码，65-90是大写英文字母，97-122是小写字母。
                    for i in range(0,10):

                        n = ''
                        for i in range(8):
                            n1 = random.randint(0,9)
                            n = n + str(n1)

                        sn = ''
                        for i in range(4):
                            s = chr(random.randint(97, 122))
                            sn = sn + s

                        cc = sn + n
                        # print('随机数为', num_p, '你输入的是',num)
                        print(cc)
                        # 执行文件存入操作
                        with open('str_num.txt','a') as f:
                            f.write(cc+'\n')
                            f.close()

                break


# 程序入口
if __name__ == '__main__':
    print(__name__)
    pass

game = MyGame()

game.num_game()









