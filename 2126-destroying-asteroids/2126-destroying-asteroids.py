class Solution(object):
    def asteroidsDestroyed(self, mass, asteroids):
        """
        :type mass: int
        :type asteroids: List[int]
        :rtype: bool
        """
        f=True
        asteroids.sort()
        for i in asteroids:
            if mass>=i:
                mass+=i
            else:
                f=False
        return f