class BSTNode:
    def delete(self, key):
        # Check if the current node is empty (has no value). If it is, return None. This represents an empty tree or a leaf node where deletion has already occurred.
        if self.val is None: 
            return None
        
        # If the value to delete is less than the current node's value:
        if key < self.val:
            
            # If there's a left child, recursively delete the value from the left subtree and update the left child reference with the result.
            if self.left is not None:
                self.left = self.left.delete(key)
            return self # Return the current node.
        if key > self.val:
            
            # If there's a right child, recursively delete the value from the right subtree and update the right child reference with the result.
            if self.right is not None:
                self.right = self.right.delete(key)
            return self # Return the current node.
        
        # If the value to delete equals the current node's value, we've found the node to delete:
        if key == self.val:
            
            # If there is no right child, return the left child. This bypasses the current node, effectively deleting it.
            if self.right is None:
                return self.left
            
            # If there is no left child, return the right child, accomplishing the same thing.
            if self.left is None:
                return self.right
            
            # If there are both left and right children, we need to find the new "successor": the smallest node in the right subtree, which is the value next largest after the current node's value.
            # Find the smallest node in the right subtree by walking down the current right child's left branches until reaching a node with no left child.
            min = self.right.get_min()
            
            # Replace the current node's value with this successor's value.
            self.val = min
            
            # Delete the successor node from the right subtree by recursively calling delete, and update the right child reference with the result.
            self.right = self.right.delete(min)
            
            # Return the current node.
            return self
        


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

    def get_min(self):
        current = self
        while current.left is not None:
            current = current.left
        return current.val

    def get_max(self):
        current = self
        while current.right is not None:
            current = current.right
        return current.val

def print_tree(bst_node):
    if bst_node is not None:
        lines = []
        format_tree_string(bst_node, lines)
        for line in lines:
            print(line)


def format_tree_string(bst_node, lines, level=0):
    if bst_node is not None:
        format_tree_string(bst_node.right, lines, level + 1)
        lines.append(" " * 4 * level + "> " + str(bst_node.val))
        format_tree_string(bst_node.left, lines, level + 1)

import os

if __name__ == "__main__":
    os.system('cls')
    lst =[10, 5, 15, 3, 7, 13, 17, 2, 4, 6, 8, 12, 14, 16, 18]
    tree = BSTNode()
    for each in lst:
        tree.insert(each)
    print_tree(tree)
    # tree.delete(10)
    for _ in range(5):
        tree.delete(tree.val)
    print('-------------------------')
    print_tree(tree)
