class store_results:
    def __init__(self, filename):
        self.filename = filename

    def __call__(self, function):
        def wrapper(*args, **kwargs):
            with open(self.filename, "a") as file:
                result = function(*args, **kwargs)
                file.write(f"Function {function.__name__} was called. Result: {result}\n")

            return result
        return wrapper


@store_results("results.txt")
def add(a, b):
    return a + b

@store_results("results.txt")
def mult(a, b):
    return a * b

add(2, 2)
mult(6, 4)