class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        arr.sort()
        minimum = float('inf') #start with the largest poss val

        for i in range(len(arr)-1): #find min diff
            diff = arr[i+1] - arr[i] #why neighbouring elements, as we have sorted the array hence neighhbourng will have most minimal difference
            if diff < minimum:
                minimum = diff

        ans = [] #stores all pairs with min diff

        for i in range(len(arr) -1):
            diff = arr[i+1] - arr[i]
            if diff == minimum:
                ans.append([arr[i], arr[i+1]])
        return ans