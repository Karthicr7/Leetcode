class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        b=str(bin(n))
        b=b[2:]
        b_32=b.zfill(32)
        a=int(b_32[::-1],2)
        return a
        