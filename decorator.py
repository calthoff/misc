def decorate(fn):
    def rf(self):
        fn(self)
        return self.bar ** 2
    return rf

class Foo():
    def __init__(self, bar):
        self.bar = bar

    @decorate
    def my_method(self):
        self.bar = self.bar * 3
        return self.bar

f = Foo(10)
print f.my_method()