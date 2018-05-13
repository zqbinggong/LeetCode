# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        '''
        找到中点，反转后半部分链表并与前半部分进行比较
        '''
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        pre = None
        while slow:
            nex = slow.next
            slow.next = pre
            pre = slow
            slow = nex
        while pre:
            if pre.val != head.val:
                return False
            pre = pre.next
            head = head.next
        return True
