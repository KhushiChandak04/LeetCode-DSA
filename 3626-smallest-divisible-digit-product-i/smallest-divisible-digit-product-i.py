class Solution(object):
    def smallestNumber(self, n, t):
        """
        :type n: int
        :type t: int
        :rtype: int
        """
        while True: #as we dont know upper limit of how many nos are there
            product = 1 #init
            for digit in str(n):
                product *= int(digit)

            if product % t == 0: #found the perfect divided ans
                return n
            n += 1