from node import Node


class LLQueue:
    def remove_from_head(self):
        if self.head is None:
            return None
        old_head = self.head
        self.head = old_head.next
        if old_head.next is None:
            self.tail = None      
        old_head.next = None      
        return old_head

    # don't touch below this line

    def add_to_tail(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
            return
        self.tail.set_next(node)
        self.tail = node

    def __init__(self):
        self.tail = None
        self.head = None

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __repr__(self):
        nodes = []
        for node in self:
            nodes.append(node.val)
        return " <- ".join(nodes)
