from pkg02 import *

# prt()  因为pkg02的__init__模块中具有 __all__ = ['p01'] 的设置, 所以这句是执行不了的
p01.say_hello()  # 如果没有__all__函数参与, 这句就执行不了, 因为*只加载__init__, 不加载其他模块.
