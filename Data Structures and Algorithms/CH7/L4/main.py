class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def size(self):
        return len(self.items)

    def peek(self):
        if self.size() == 0:
            return None
        return self.items[-1]

    def pop(self):
        if self.size() == 0:
            return None
        top = self.peek()
        del self.items[-1]
        return top

if __name__ == "__main__":
    arr = Stack()
    arr.push(None)
    print(arr.items)
    print(arr.pop())
    print(arr.items, arr.size())
