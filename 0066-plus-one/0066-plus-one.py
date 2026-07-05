class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        s = ''.join(map(str,digits))
        a=int(s)
        a=a+1
        return [int(ch) for ch in str(a)]
        