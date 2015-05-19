def decorate(fn):
    def rf(self):
        return self.bar ** 2
    return rf

class Foo():
    def __init__(self, bar):
        self.bar = bar

    @decorate
    def my_method(self):
        return self.bar

f = Foo(100)
print f.my_method()