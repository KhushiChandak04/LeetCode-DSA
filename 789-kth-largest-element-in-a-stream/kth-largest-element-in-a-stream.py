class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k

        #make min heap
        self.heap = nums
        heapq.heapify(self.heap)

        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        #add a new number
        heapq.heappush(self.heap, val)
        #if we have more than k numbers we remove the smallest
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)

        return self.heap[0] #smallest element in the heap is kth element
        
# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)