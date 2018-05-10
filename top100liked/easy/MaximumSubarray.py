class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxSum = curSum = nums[0]
        for num in nums[1:]:
            curSum = max(curSum + num, num)
            maxSum = max(maxSum, curSum)
        return maxSum