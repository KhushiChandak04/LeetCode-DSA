class Solution(object):
    def elevatorRequests(self, n, requests):
        """
        :type n: int
        :type requests: List[int]
        :rtype: int
        """
        floor = 0 #initilise
        time = 0 #total time taken

        for request in requests:
            time += abs(floor - request)
            floor = request
        return time