class BSTNode:
    def exists(self, val):
        if self.val == val:
            return True
        elif self.left and val < self.val:
            return self.left.exists(val)
        elif self.right and val > self.val:
            return self.right.exists(val)
        else:
            return False

        # don't touch below this line

    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val

    def insert(self, val):
        if not self.val:
            self.val = val
            return

        if self.val == val:
            return

        if val < self.val:
            if self.left:
                self.left.insert(val)
                return
            self.left = BSTNode(val)
            return

        if self.right:
            self.right.insert(val)
            return
        self.right = BSTNode(val)

if __name__ == "__main__":
    nodes = [10, 11]
    tree = BSTNode()
    for each in nodes:
        tree.insert(each)
    print(tree.exists(9))