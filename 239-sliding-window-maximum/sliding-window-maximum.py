class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        q = deque() #double ended queue
        answer = [] #stores maximum of every window

        for i in range(len(nums)):
            #remove indices outside of the windw
            if q and q[0] <= i-k:
                q.popleft()

            #remove smaller numbers from the back
            while q and nums[q[-1]] <= nums[i]:
                q.pop() #pop right
            
            #add current index
            q.append(i)

            #once the window size becomes k
            if i >= k-1:
                answer.append(nums[q[0]])
        return answer

        ### brute force approach is where we can use max(window) where window is nums[i:i+k]but it will give TLE issue as its complexity will be o(n*k)