class Solution(object):
    def mapWordWeights(self, words, weights):
        """
        :type words: List[str]
        :type weights: List[int]
        :rtype: str
        """
        s=""
        for i in words:
            sum=0
            for j in i:
                position = ord(j.lower()) - ord('a') 
                sum+=weights[position]
            p=sum%26
            letter = chr(ord('z') - p)
            s+=letter
        return s
