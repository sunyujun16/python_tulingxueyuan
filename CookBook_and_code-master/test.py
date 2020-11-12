class MappingMixin:
    def __getitem__(self, key):
        return self.__dict__.get(key)

    # def __setitem__(self, key, value):
    #     return self.__dict__.set(key, value)
    pass


class Person(MappingMixin):
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age


p = Person("小陈", "男", 18)
print(p.name)
print(p['name'])
print(p['age'])