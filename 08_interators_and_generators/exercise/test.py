class MyIterator:
    def __init__(self, iterable):
        self.iterable = iterable
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter < len(self.iterable):
            self.counter += 1
            return self.iterable[self.counter - 1] * 2
        else:
            raise StopIteration()

ls = [1, 2, 3, 4, 5]
iterator = MyIterator(ls)

# for i in iterator:
#     print(i)

print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))


def my_generator(iterator):
    for num in iterator:
        yield num * 2

my_gen = my_generator(ls)

for i in my_gen:
    print(i)

