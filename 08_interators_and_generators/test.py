# text = "hello there"
#
# for char in text:
#     print(char)
#
# class Person:
#     def __init__(self, name, age) -> None:
#         self.name = name
#         self.age = age
#         self.start = -1
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         self.start += 1
#         if self.start < len(self.name):
#             return self.name[self.start]

#         raise StopIteration
#
# p = Person("Ivan", 35)
#
# for el in p:
#     print(el)
#
# def custom_range(start, end):
#     current = start
#     while current <= end:
#         yield current
#         current += 1
# one_to_ten = custom_range(1, 10)
# for num in one_to_ten:
#     print(num)
