# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is null:
            return True
        stack = [[root.left, root.right]]
        while len(stack) > 0:
            pair = stack.pop(0)
            left = pair[0]
            right = pair[1]
            if left is null and right is null:
                return True
            if left is null or right is null:
                return False
            if left.value != right.value:
                return False
            # 栈和递归的等效，需注意到入栈的顺序必须指定好
            stack.insert([left.left, right.right])
            stack.insert([left.right, right.left])
        return True
        
