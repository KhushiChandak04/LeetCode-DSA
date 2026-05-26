class Solution(object):
    def hammingWeight(self, n):
        count = 0 #initialise
        while n:
            n &= n-1 #use logical AND and the shift it
            count += 1
        return count