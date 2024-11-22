class Pila:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        raise IndexError("La pila está vacía")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        raise IndexError("La pila está vacía")

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)
