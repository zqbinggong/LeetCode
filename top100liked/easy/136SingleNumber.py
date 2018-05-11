class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for num in nums[1:]:
            nums[0] ^= num
        return num
