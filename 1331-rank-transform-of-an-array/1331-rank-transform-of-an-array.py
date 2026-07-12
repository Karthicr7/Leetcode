class Solution(object):
    def arrayRankTransform(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        l = sorted(set(arr))

        op={}
        for i, num in enumerate(l):
            op[num] = i + 1
        return [op[x] for x in arr]


        