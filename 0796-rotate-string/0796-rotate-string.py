class Solution(object):
    def rotateString(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        f=0
        for i in range(len(s)):
            r=s[i:]+s[:i]
            if r==goal:
                f=1
                return True
        if f==0:
            return False