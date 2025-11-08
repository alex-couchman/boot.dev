class Queue:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.size() == 0:
            return None
        item = self.items[0]
        del self.items[0]
        return item

    def peek(self):
        if self.size() == 0:
            return None
        return self.items[0]

    def size(self):
        return len(self.items)
