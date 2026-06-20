class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        prefix = 0 #prefix sum till curr index
        count = 0 #total sub arrays with sum k
# prefix_sum : number of times it has appeared
        #
        # {0:1} means:
        # before starting the array, prefix sum 0 has occurred once
        # this helps count subarrays starting from index 0
        hashmap = {0:1}
        for num in nums:
            prefix += num
            if prefix - k in hashmap:
                count += hashmap[prefix - k]
            hashmap[prefix] = hashmap.get(prefix, 0) + 1 #store it
        return count