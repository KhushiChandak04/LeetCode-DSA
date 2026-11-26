
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n <= 2:
            return 0

        prime = [True] * n

        prime[0] = False #base case
        prime[1] = False

        for i in range(n):
            if prime[i]:
                for j in range(i*i, n, i):
                    prime[j] = False

        ans = 0
        for i in range(n):
            if prime[i]:
                ans += 1

        return ans