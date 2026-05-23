class Solution(object):

#function to return their indices 
    def twoSum(self, arr, target):
        n = len(arr)
        for i in range (n):
            for j in range (i+1, n):
                if arr[i] + arr[j] == target:
                    return [i,j]
        return [-1,-1]

if __name__ == "__main__":
    sol = Solution()
    arr = [2,7,11,15]
    target = 9
    print(sol.twoSum(arr, target))
