# 复习

''' math模块:
向上取整,向下取整,查看系统保留的关键词,四舍五入，开平方,幂运算,求绝对值,
Python内置求和,把数分解为浮点数和整数的元组,将第二个参数的符号赋予第一个数,获取0-1之间的随机小数
'''
import math
'''
# 向上取整
print(math.ceil(5.88)) #返回整型

# 向下取整
print(math.floor(5.88)) #也是整型

# 查看系统保留关键词，不能用于变量命名
import keyword
print(keyword.kwlist)

# 四舍五入,这个不是math模块下的，而是Python内建函数
print(round(5.12,1))# 第二个参数控制小数点后几位

# 开平方
print(math.sqrt(256)) # return float

# 幂运算
print(math.pow(2,8)) # return integer

# 放飞一下
print(math.sqrt(math.pow(16,2))) # bingo~!

# 求绝对值，两种
print(math.fabs(-3.15))
print(math.fabs(-6)) #返回浮点数
print(abs(-6))
print(abs(-3.15)) # 返回原型

# 求和，两种
print(math.fsum([1,2,3])) # 返回浮点数
print(sum([1,2,3])) # 返回原型

# 把数分解为浮点数和整数的元组
print(math.modf(3.1415)) # 返回浮点数，小数在前，怎么去掉多余的小数点位呢？显然没有更多参数来控制这个

# 将第二个参数的符号赋予第一个数
print(math.copysign(1,-3.25)) # return a float
OK，第一次复习成功！
'''

import random

'''random 模块：
获取0-1之间的随机小数,必须先import random模块（random module）
随机获取指定区间的整数值，可以指定间隔
随机获取列表中的值
洗牌，打乱顺序
随机获取指定范围内的值

# 获取0-1之间的随机小数,必须先import random模块（random module）
import random
print(random.random())

# 随机获取指定区间的整数值,两种，其中一种可以指定间隔
for _ in range(0,10):
    print(random.randint(2,9),end=',')

print()
print('='*20)

for _ in range(0,10):
    print(random.randrange(2,9,2),end=',')
    
print()
print('='*20)

# 随机获取列表中的值
print(random.choice([1,2,3,5,5,8,54,4]))
print(random.choice((1,2,4,5,4)))
# set不可以 --- print(random.choice({1,5,4,4,6}))
# dict也不可以 --- print(random.choice({'one':1,'two':2,'three':3}))

# 洗牌，打乱顺序,return 一个 None
l1 = [2,1,45,65,24,5,5,4,5,45,4,85,1]
print(l1)
random.shuffle(l1)
print(l1)

# 随机获取指定范围内的值
print(random.uniform(0,5)) # 就这两个参数，控制不了小数点位
random复习完成
'''







