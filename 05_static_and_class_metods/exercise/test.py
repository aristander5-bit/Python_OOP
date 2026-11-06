class MyClass:
    def __init__(self, name: str):
        self.name = name

    @classmethod
    def my_class_method(cls):
        return cls("Ivan")

    @staticmethod
    def my_static_method():
        return "This is a static method"


o = MyClass.my_class_method()
print(o.my_static_method())