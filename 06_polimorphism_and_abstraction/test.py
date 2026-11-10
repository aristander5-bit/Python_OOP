class Shape:
    def calculate_area(self):
        return None

class Square(Shape):
    def __init__(self, side):
        self.side = side
    def calculate_area(self):
        return self.side * 2

class Triangle(Shape):
    def __init__(self, side, height):
        self.side = side
        self.height = height
    def calculate_area(self):
        return 0.5 * self.side * self.height

shapes = [Triangle(3, 6), Square(2), Square(7), Triangle(1, 8)]
for shape in shapes:
    print(shape.calculate_area())



from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    @abstractmethod
    def greet(self):
        pass
        
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        if len(value) < 2:
            raise ValueError("Name must be at least 2 characters long")
        self.__name = value

    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, value):
        if value <= 0:
            raise ValueError("Age cannot be negative")
        self.__age = value

class Player(Person):
    def greet(self):
        return f"Hi i'm a player with name {self.name} and age {self.age}"

class Teacher(Person):
    def greet(self):
        return f"Hi i'm a teacher with name {self.name} and age {self.age}"

for obj in [Teacher("Ivan", 50), Player("Pesho", 20)]:
    print(obj.greet())
