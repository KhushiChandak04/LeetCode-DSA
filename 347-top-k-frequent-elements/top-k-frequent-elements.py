import heapq #python inbuilt library for heap
#heap is a special data structure that stores a smallest number at top
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count = {} #empty dictionary
        for num in nums:
            count[num] = count.get(num,0) + 1 #key value pair for dictionary
        heap = [] #empty heap -> freq:num
        for num in count:
            heapq.heappush(heap, (count[num], num)) #push key value pair into heap
            if len(heap) > k:
                heapq.heappop(heap) #remove smallest freq as we want onli top k here in heap
        return [num for freq, num in heap]