class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        #greedy algo -> start with 1 1 1 candies, and traverse for both neighbours

        n = len(ratings)
        candies = [1] * n #dp array

        #left to right traversal such that higher rated candidate gets more candy
        for i in range(1,n):
            if ratings[i] > ratings[i-1]: #higher rating than left neighbour
                candies[i] = candies[i-1] + 1
        
        #right to left travesal such that hogher rated child gets more candy
        for i in range(n - 2, -1, -1): #right to left traversal (start, stop, step) format
            if ratings[i] > ratings[i+1]:
                candies[i] = max(candies[i], candies[i+1] + 1)

        return sum(candies)