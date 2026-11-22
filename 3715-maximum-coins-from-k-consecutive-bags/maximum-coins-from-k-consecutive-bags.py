from bisect import bisect_left, bisect_right

class Solution(object):
    def maximumCoins(self, coins, k):
        """
        :type coins: List[List[int]]
        :type k: int
        :rtype: int
        """
        # here the range is given in [l,r,c] format
        # we will have to sort coins according to their starting point first
        coins.sort()
        n = len(coins)

        starts = []
        ends = []
        prefix = [0]

        for l,r,c in coins:
            starts.append(l)
            ends.append(r)

            total = (r-l+1)*c
            prefix.append(prefix[-1]+total)

        def get_coins(left,right):

            #find first and last segments in the window
            i = bisect_left(ends,left)
            j = bisect_right(starts,right)-1

            if i>j:
                return 0

            if i==j:
                length = min(right,ends[i])-max(left,starts[i])+1
                return length*coins[i][2]

            # coins from first and last segments
            first_length = ends[i]-max(left,starts[i])+1
            total = first_length*coins[i][2]

            last_length = min(right,ends[j])-starts[j]+1
            total += last_length*coins[j][2]

            # add complete segments in between using prefix sum
            total += prefix[j]-prefix[i+1]
            return total

        ans = 0

        # check windows starting and ending at segment boundaries
        for l,r,c in coins:
            ans = max(ans,get_coins(l,l+k-1))
            ans = max(ans,get_coins(r-k+1,r))

        return ans