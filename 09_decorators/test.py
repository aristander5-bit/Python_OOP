# def hello_function():
#     def say_hi():
#
#         return "Hi"
#     return say_hi
#
# hello = hello_function()
# print(hello()):

def my_decorator_with_parameters(arg1, arg2):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print("Start decorator function")
            func(*args, **kwargs)
            print("End decoration function")
        return wrapper
    return decorator

@my_decorator_with_parameters("a1", "a2")
def my_func():
    print("This is my function")

my_func()
