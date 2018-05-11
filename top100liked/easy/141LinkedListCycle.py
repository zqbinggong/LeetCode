# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
'''
说白了就好似给定一个多边形，让两个点在上面绕着相同方向以不同的速度走，最终让其相遇
相对速度取为1,否则两者可能不会相遇
由于无法决定多边形的起点，因而必须两者都要移动
'''
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        try:
            slow = head
            fast = head.next
            while head is not slow:
                slow = slow.next
                fast = fast.next.next
        except:
            return True
        return False
        
