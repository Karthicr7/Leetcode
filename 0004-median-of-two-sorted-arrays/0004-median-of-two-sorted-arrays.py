class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums1+=nums2
        nums1.sort()
        if len(nums1)%2!=0:
            return nums1[len(nums1)//2]
        else:
            a=len(nums1)//2
            b=a-1
            return (nums1[a]+nums1[b])/2.0
        