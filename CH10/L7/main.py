class BSTNode:
    def get_min(self): # recursive approach
        if self.left is None:
            return self.val
        return self.left.get_min()
    
    # def get_min(self): # non-recursive approach
    #     min = self.val
    #     while self.left is not None:
    #         min = self.left.val
    #         self = self.left
    #     return min

    def get_max(self): # recursive approach
        if self.right is None:
            return self.val
        return self.right.get_max()
    
    # def get_max(self): # non-recursive approach
    #     max = self.val
    #     while self.right is not None:
    #         max = self.right.val
    #         self = self.right
    #     return max

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

