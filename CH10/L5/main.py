class BSTNode:
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val
        if val is not None:
            self.root = self

    def insert(self, val):
        if self.val is None:
            self.val = val
            self.root = self
        elif self.val == val:
            pass
        elif val < self.val:
            if self.left is None:
                self.left = BSTNode(val)
            else:
                self.left.insert(val)
        else:
            if self.right is None:
                self.right = BSTNode(val)
            else:
                self.right.insert(val)
                
    def inorder_print(self):
        self._inorder_recursive(self.root)
        print() # For a newline after printing

    def _inorder_recursive(self, node):
        if node:
            self._inorder_recursive(node.left)
            print(node.val, end=" ")
            self._inorder_recursive(node.right)


if __name__ == "__main__":
    
    bintree = BSTNode(10)
    nums = [5, 9, 10, 12, 15]
    nums = [100, 25, 10, 12, 15]
    for num in nums:
        bintree.insert(num)
    bintree.inorder_print()