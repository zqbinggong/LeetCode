class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        '''
        注意，python3中的range直接就是python2中的xrange，原本的range可以使用list(range())实现
        '''
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[j] = nums[i]
                j += 1
        for j in range(j, len(nums)):
            nums[j] = 0
            
        
