
class Solution(object):
    def getLargestOutlier(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = sum(nums)

        count = {} #create a dict to store freq

        for num in nums: #store vals in dict
            if num in count:
                count[num] += 1
            else:
                count[num] = 1

        ans = float('-inf')

        for num in nums:
            remaining = total - num

            #special sum must be an integer
            if remaining % 2 != 0:
                continue

            special_sum = remaining // 2

            if special_sum in count:

                if special_sum != num or count[num] > 1:
                    ans = max(ans, num)

        return ans