# import 01
# stu = 01.Student()

import importlib

tuling = importlib.import_module("01")

stu = tuling.Student()

stu.say()