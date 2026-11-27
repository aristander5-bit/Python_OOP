from abc import ABC, abstractmethod


class Graphic(ABC):
    @abstractmethod
    def draw(self):
        pass

class Circle(Graphic):
    def draw(self):
        print('drawing circle')

class Square(Graphic):
    def draw(self):
        print('drawing square')

class CompositeGraphic(Graphic):
    def __init__(self):
        self.children = []

    def add(self, graphic: Graphic):
        self.children.append(graphic)

    def remove(self, graphic: Graphic):
        self.children.remove(graphic)

    def draw(self):
        for child in self.children:
            child.draw()

c1 = Circle()
c2 = Circle()
s = Square()

composite = CompositeGraphic()

composite.add(c1)
composite.add(c2)
composite.add(s)

composite.draw()
print("===============")
composite.remove(c1)
composite.draw()


class Light:
    def on(self):
        print('on')

    def off(self):
        print('off')

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

class LightOnCommand(Command):
    def __init__(self, light: Light):
        self.light = light

    def execute(self):
        self.light.on()

class LightOffCommand(Command):
    def __init__(self, light: Light):
        self.light = light

    def execute(self):
        self.light.off()

class RemoteControl:
    def __init__(self):
        self._command = {}

    def set_command(self, button, command):
        self._command[button] = command

    def push_button(self, button):
        self._command[button].execute()

light = Light()

light_on = LightOnCommand(light)
light_off = LightOffCommand(light)

remote = RemoteControl()
remote.set_command("ON", light_on)
remote.set_command("OFF", light_off)

remote.push_button("ON")
remote.push_button("OFF")

