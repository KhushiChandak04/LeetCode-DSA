import heapq
class Solution(object):
    def mincostToHireWorkers(self, quality, wage, k):
        """
        :type quality: List[int]
        :type wage: List[int]
        :type k: int
        :rtype: float
        """

        workers = []   # Store (ratio, quality) for every worker
        for i in range(len(quality)):
            ratio = float(wage[i]) / quality[i]
            workers.append((ratio, quality[i]))   # Tuple

        # Sort workers by ratio (smallest to largest)
        workers.sort()

        heap = []                # Max heap (stores negative qualities)
        quality_sum = 0          # Running sum of qualities
        answer = float("inf")    # Stores minimum cost

        # Process every worker one by one
        for worker in workers:
            ratio = worker[0]
            q = worker[1]

            # Add current worker's quality
            # Store negative because Python has only a min heap
            heapq.heappush(heap, -q)
            quality_sum += q

            # If more than k workers, remove the worker
            # having the largest quality
            if len(heap) > k:
                largest_quality = -heapq.heappop(heap)
                quality_sum -= largest_quality

            # If exactly k workers, calculate hiring cost
            if len(heap) == k:
                cost = ratio * quality_sum
                if cost < answer:
                    answer = cost

        return answer