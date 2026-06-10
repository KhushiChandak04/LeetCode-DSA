class Solution(object):
    def getWinner(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        winner = arr[0] #base condition
        wins = 0 #initialise
        for i in range(1, len(arr)):
            if winner > arr[i]:
                wins += 1
            else:
                winner = arr[i]  #traverse ahead
                wins = 1
            if wins == k:
                return winner
        return winner