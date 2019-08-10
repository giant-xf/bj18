class Sing(object):
    __instance =None

    def  __new__(cls, age, name):

        if not cls.__instance:
            cls.__instance=object.__new__(cls)

        return cls.__instance

a =Sing(14,'aaaa')
b =Sing(12,'bbbb')

print(id(a))
print(id(b))

a.age =13
print(b.age)