class Solution(object):
    def beautifulSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #XOR becomes 0 when there are even nos of 1's and here we actually need to have pairs to make anything 0, so we are actually taking xor of the subarray -> beautiful
        prefix_xor = 0
        count = 0
        hashmap = {0: 1} #prefix_xor : freq
        for num in nums:
            prefix_xor ^= num
            count += hashmap.get(prefix_xor, 0)
            hashmap[prefix_xor] = hashmap.get(prefix_xor, 0) + 1 #fill values in hashmap
        return count