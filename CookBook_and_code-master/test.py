# 那么怎么能让赋值有用呢，想必是要在描述符的函数内下功夫

class Descriptors():

    def __init__(self, key, value_type):
        self.key = key
        self.value_type = value_type

    def __get__(self, instance, owner):
        print("执行Descriptors的get")
        return instance.__dict__[self.key]

    def __set__(self, instance, value):
        print("执行Descriptors的set")
        if not isinstance(value, self.value_type):
            raise TypeError("参数%s必须为%s" % (self.key, self.value_type))
        instance.__dict__[self.key] = value

    def __delete__(self, instance):
        print("执行Descriptors的delete")
        instance.__dict__.pop(self.key)


class Person():
    name = Descriptors("芳名", str)
    age = Descriptors("芳龄", int)

    # 这两句使得name和age和上面有了关联，在对他俩进行调用或者设置时，就会自动跳转上面，而忽略下面。

    def __init__(self, name0, age0):
        self.name = name0
        self.age = age0


person = Person("奕含", 26)
print(person.name)
# 这里打出了奕含，要知道，尽管跳转到上面的描述符，但是描述符仍然是作为一个整体，而在Person class内部运行的，这就是为什么明明是
# set函数对参数进行了处理，结果却会反应到person的属性当中。其对应关系应该是：self无意义，instance对person，value对参数
# 而name = Descriptors("name", str)这个对应了Deacriptors的__init__函数，’name‘为key，str为value_type。
print('=' * 50)

print(person.__dict__)  #
print(Person.__dict__)  # 注意value的具体值，奕含，只是加到了实例的属性当中
print('=' * 50)

print(person.name)  #
print('=' * 50)

person.name = "jone"  #
print(person.__dict__)

# 到这儿基本就明白了，呼～可以午睡了

# 20201111复习纠正: name 是Descriptors的实例,这是关键点, 当打印person.name的时候
# 实际上是在打印__get__函数的返回值, 这些值来来回回都是在Descriptors内部赋值的.从下面的__dict__结果中也能看出这点
# 那么,描述符,实际上就是把属性设定成描述符类的实例这么个事儿.
# 果然温故而知新呐