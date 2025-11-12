class BSTNode:
    def height(self):
        if not self.val:
            return 0
        left_height = 0
        if self.left:
            left_height = self.left.height()
        right_height = 0
        if self.right:
            right_height = self.right.height()
        return max(left_height, right_height) + 1

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
