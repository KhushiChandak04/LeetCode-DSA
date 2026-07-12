class Solution(object):
    def arrayRankTransform(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        sorted_array = sorted(set(arr))
        rank = {}
        current_rank = 1 #initilise this

        for num in sorted_array:
            rank[num] = current_rank
            current_rank += 1
        
        #replace every element with its rank
        answer = []
        for num in arr:
            answer.append(rank[num])
        return answer