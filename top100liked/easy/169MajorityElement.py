class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        关键在于，major出现的次数大于一半
        """
        '''# time O(n),space O(n)
        if len(nums) == 1:
            return nums[0] 
        buff_dict = {}
        m = int(len(nums) / 2)
        for num in nums[:]:
            if num in buff_dict:
                if buff_dict[num] == m:
                    return num
                else:
                    buff_dict[num] += 1
            else:
                buff_dict[num] = 1
        '''
        '''
        # time sorted, space 0
        return sorted(nums)[len(nums) / 2]
        '''
        # time O(n), space O(1)
        major = nums[0]
        count = 1
        for num in nums[1:]:
            if count == 0:
                count = 1
                major = num
            elif major == num:
                count += 1
            else:
                count -= 1
        return major
