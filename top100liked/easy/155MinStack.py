class MinStack:
    '''
    1. 最小元素不能简单用一个额外的量指定，因为这个量可能会被pop掉
    2. 同1, 需要注意到当栈被pop成空栈时，此时的最小元素需要更新
    '''

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.q = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        minEle = self.getMin()
        if minEle is None or x < minEle:
            minEle = x
        self.q.insert(0, [minEle, x])
        

    def pop(self):
        """
        :rtype: void
        """
        if len(self.q) > 0:
            self.q.pop(0)
        

    def top(self):
        """
        :rtype: int
        """
        if len(self.q) == 0:
            return None
        return self.q[0][1]
        

    def getMin(self):
        """
        :rtype: int
        """
        if len(self.q) == 0:
            return None
        return self.q[0][0]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
