class Bar(object):
    pass


class Foo(object):
    """  这是个类"""
    def __init__(self):
        pass

    def __getattr__(self, item):
        print(item,end=" ")
        return self

    def __str__(self):
        return ""

if __name__ == '__main__':
    print(Foo().think.deffrent.itcast)


