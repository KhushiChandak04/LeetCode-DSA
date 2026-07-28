class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph = {i : [] for i in range(numCourses)} #build an adjacency list
        for course, prereq in prerequisites:
            graph[prereq].append(course) #this creates a graph

        # 0 = visited, 1 = current node, 2 = fully visited
        state = [0] * numCourses #dp array of courses init
        def dfs(course):
            if state[course] == 1:
                return False #cycle found
            if state[course] == 2:
                return True #already processed
            state[course] = 1 #current visited
            #visit all next nodes
            for next in graph[course]:
                if not dfs(next):
                    return False
            state[course] = 2 #mark as completely filled after travesing all nodes
            return True
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True