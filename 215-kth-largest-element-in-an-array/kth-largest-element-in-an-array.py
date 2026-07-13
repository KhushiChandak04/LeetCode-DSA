class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        #without sorting, we use min-heap here 
        heap = []
        for num in nums:
            heapq.heappush(heap, num)

            if len(heap) > k: #keep onli k largest element in min heap
                heapq.heappop(heap) #when size exceeds k, remove the smallest
        
        #whatever remains is kth largest element in the heap, so return heap top
        return heap[0]