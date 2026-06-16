class Solution(object):
    def mapWordWeights(self, words, weights):
        """
        :type words: List[str]
        :type weights: List[int]
        :rtype: str
        """
        letters = {25: 'a', 24: 'b', 23: 'c', 22: 'd', 21: 'e', 20: 'f', 19: 'g', 18: 'h', 17: 'i', 16: 'j', 15: 'k', 14: 'l', 13: 'm', 12: 'n', 11: 'o', 10: 'p', 9: 'q', 8: 'r', 7: 's', 6: 't', 5: 'u', 4: 'v', 3: 'w', 2: 'x', 1: 'y', 0: 'z'}

        s=""
        for i in words:
            sum=0
            for j in i:
                position = ord(j.lower()) - ord('a') 
                sum+=weights[position]
            p=sum%26
            s+=letters[p]
        return s
