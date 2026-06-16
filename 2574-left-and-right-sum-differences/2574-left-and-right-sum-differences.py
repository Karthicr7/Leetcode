class Solution(object):
    def leftRightDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        d=[]
        for i in range(0,len(nums)):
            l=sum(nums[0:i])
            r=sum(nums[i+1:])
            d.append(abs(l-r))
        return d
        