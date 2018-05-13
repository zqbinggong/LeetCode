# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        '''
        可以简化代码，即无需判断是否为空直接入栈，然后在while循环的开端进行判断即可
        '''
        if root is None:
            return root
        stack = [root]
        
        while len(stack) > 0:
            p = stack.pop(0)
            left = p.left
            right = p.right
            if left is None and right is None:
                continue
            elif left is None:
                p.left = right
                p.right = None
                stack.insert(0, p.left)
            elif right is None:
                p.right = left
                p.left = None
                stack.insert(0, p.right)
            else:
                temp = p.left
                p.left = p.right
                p.right = temp
                stack.insert(0, p.left)
                stack.insert(0, p.right)
        return root
                
                
                
                
