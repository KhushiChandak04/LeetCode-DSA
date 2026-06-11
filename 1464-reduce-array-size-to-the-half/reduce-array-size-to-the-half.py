class Solution(object):
    def minSetSize(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        count = {} #initialise blank count
        n = len(arr)
        for num in arr:
            count[num] = count.get(num, 0) + 1
        freq = sorted(count.values(), reverse = True) #descending order
        removed = 0
        for i in range(len(freq)):
            removed += freq[i]
            if removed >= n // 2:
                return i+1