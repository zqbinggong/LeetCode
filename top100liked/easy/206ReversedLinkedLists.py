class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 简洁版
        last = now = 0
        for num in nums:
            last, now = now, max(num + last, now)
        return now
        
        '''
        # 一般的动态规划，这里还可以优化，因为没必要从尾部开始，因为从街头开始抢劫和从街尾开始抢劫一样
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[n-2], nums[n-1])
        
        amount = [0 for i in range(n)]
        amount[n-1] = nums[n-1]
        amount[n-2] = max(nums[n-2], nums[n-1])
        amount[n-3] = max(nums[n-3] + nums[n-1], nums[n-2])
        
        for i in range(4, n+1):
            temp1 = nums[n-i] + amount[n-i+2]
            temp2 = nums[n-i+1] + amount[n-i+3]
            amount[n-i] = max(temp1, temp2)
        
        return amount[0]
        '''
