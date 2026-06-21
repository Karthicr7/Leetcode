class Solution(object):
    def maxIceCream(self, costs, coins):
        """
        :type costs: List[int]
        :type coins: int
        :rtype: int
        """
        costs.sort()
        sum=0
        k=0
        for i in costs:
            if (sum+i)<=coins:
                sum+=i
                k+=1
        return k
        