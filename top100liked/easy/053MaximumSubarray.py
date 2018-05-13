# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        l = self.maxSubDep(1,root.left)
        r = self.maxSubDep(1,root.right)
        return l if l>r else r
    
    def maxSubDep(self, d, root):
        if root is None:
            return d
        d += 1
        l = self.maxSubDep(d, root.left)
        r = self.maxSubDep(d, root.right)
        return l if l > r else r
