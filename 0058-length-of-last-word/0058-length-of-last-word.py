class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        l1=list(s.split())
        for i in range(0,len(l1)):
            if(i==len(l1)-1 and l1[i]!=" "):
                return len(l1[i])

        
        