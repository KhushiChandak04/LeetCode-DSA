class Solution(object):
    def reverseBits(self, n):
        #Extract the last bit using n&1, shift it to its reversed position using <<, add it into result using OR, then right shift n using >> to process the next bit.
        result = 0
        for i in range (32):
            result |= (n&1) << (31-i)
            n = n>>1
        return result