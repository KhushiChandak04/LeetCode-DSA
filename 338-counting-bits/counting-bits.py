class Solution(object):
    def countBits(self, n):
        ans = list() #list initialised
        for i in range (n+1):
            ans.append(bin(i).count('1')) #bin is used for converting to binary string and count is counting 1 everytime, append is used to add element to end of the list
        return ans