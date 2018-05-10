class ListNode:
    def __init__(self, x):
        self.value = x
        self.next = None


class Solution:
    def mergeTwoLists(self, a, b):
        """
        :param b:
        :param a:
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if a and b:
            if a.value > b.value:
                a, b = b, a
            a.next = self.mergeTwoLists(a.next, b)
        return a or b
