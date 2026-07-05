class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target>nums[-1]:
            return len(nums)
        if target in nums:
            return nums.index(target)
        else:
            for i in range(0,len(nums)):
                if nums[i]>target:
                    return i
        