class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        n = len(isConnected)
        visited = [False] *n
        ans = 0

        def dfs(city):
            visited[city] = True #mark current city as visited
            for next_city in range(n):
                if isConnected[city][next_city] == 1 and not visited[next_city]:
                    dfs(next_city) #visit connected city
        
        for city in range(n):
            if not visited[city]:
                ans += 1 #new unvisited city, new province
                dfs(city)
        return ans