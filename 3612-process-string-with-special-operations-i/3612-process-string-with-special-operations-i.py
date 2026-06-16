class Solution(object):
    def processStr(self, s):
        """
        :type s: str
        :rtype: str
        """
        newstr=""

        for i in s:
            if i.islower():
                newstr+=i
            if i=='*':
                if newstr!="":
                    l=len(newstr)
                    newstr=newstr[:l-1]
            elif i=='#':
                if newstr!="":
                    newstr+=newstr[:]
            elif i=='%':
                if newstr!="":
                    newstr=newstr[::-1]
        return newstr
