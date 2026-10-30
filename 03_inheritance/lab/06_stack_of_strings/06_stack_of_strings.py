class Stack:
    def __init__(self):
        self.data: list = []

    def push(self, item):
        self.data.append(item)

    def pop(self):
        return self.data.pop()

    def top(self):
        return self.data[-1]

    def is_empty(self):
        return not any(self.data)

    def __str__(self):
        return f"[{', '.join(reversed(self.data))}]"

s = Stack()

s.push("1")
s.push("2")
s.push("3")
print(s)
s.pop()
print(s)
