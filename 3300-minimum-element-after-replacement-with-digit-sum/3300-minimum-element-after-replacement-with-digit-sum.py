class Solution(object):
    def minElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=[]
        for i in nums:
            s=0
            while i>0:
                s+=i%10
                i//=10
            l.append(s)
        return min(l)

    