class Solution:
    def twoSum(self, nums, target):
        """
        注意到，查找字典中的key是哈系的，故而是O（1）
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) <= 0:
            return False
        buff_dict = {}
        for i in range(len(nums)):
            if nums[i] in buff_dict:
                return [buff_dict[nums[i]], i]
            else:
                buff_dict[target - nums[i]] = i
