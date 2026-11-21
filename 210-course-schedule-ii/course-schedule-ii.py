class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        #core idea - schedule 1 + topological sort
        graph = [[] for i in range(numCourses)]
        indegree = [0]*numCourses #stores num of prereq

        for a,b in prerequisites:
            graph[b].append(a) #b should be finished before a
            indegree[a] += 1 #incr count of a

        q = deque() #two way queue to store course with no prereq

        for i in range(numCourses):
            if indegree[i] == 0: #if no prereq, then append i
                q.append(i)
        
        ans = []

        while q:
            node = q.popleft() #take course with 0 prereq
            ans.append(node) #add this to our queue

            for nei in graph[node]: #chk all nodes that depend on this node in graph
                indegree[nei] -= 1 #if prereq completed reduce it by 1

                if indegree[nei] == 0:
                    q.append(nei)

        if len(ans) == numCourses:
            return ans
        return []