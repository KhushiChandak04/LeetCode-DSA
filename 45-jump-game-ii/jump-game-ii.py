class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        jumps = 0 #initilise
        current_end = 0 #end of current jump's end
        farthest = 0 #highest index

        for i in range(len(nums) -1 ): #no need to process last element, as we cannot jump after that
            farthest = max(farthest, i + nums[i]) #jump
            if i == current_end:
                #take another jump
                jumps += 1
                current_end = farthest
        return jumps