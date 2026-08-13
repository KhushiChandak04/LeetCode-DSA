class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        count = {} #dictionary initilise
        for task in tasks:
            count[task] = count.get(task, 0) + 1 #standard format to get the count value, to count the no of tasks here as its string
        max_count = max(count.values()) #find the biggest count here
        ans = (max_count - 1) * (n+1)

        for i in count.values():
            if i == max_count:
                ans += 1 #add the tasks that have the same maximum frequency
        return max(len(tasks), ans) #return total tasks or calculated intervals, whichever is bigger