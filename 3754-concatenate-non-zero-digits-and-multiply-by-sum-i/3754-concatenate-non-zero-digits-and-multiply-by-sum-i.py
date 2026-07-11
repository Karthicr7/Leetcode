class Solution(object):
    def sumAndMultiply(self, n):
        """
        :type n: int
        :rtype: int
        """
        s=str(n)
        if s.count('0')==len(s):
            return 0
        l=s.split('0')
        news="".join(l)
        sum1=0
        for x in news :
            sum1+=int(x)
        return sum1*int(news)
        