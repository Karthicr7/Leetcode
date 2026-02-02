class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        a=len(needle)
        f=0
        for i in range(0,len(haystack)):
            if(haystack[i:a+i]==needle and i<=(len(haystack) - a)):
                f=1
                b=i
                break
        if haystack==needle:
            return 0
        if(f!=0):
            return b
        else:
            return -1
                