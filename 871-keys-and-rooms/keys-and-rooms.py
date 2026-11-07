class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        n = len(rooms)

        visited = [False] * n
        stack = [0] #start from room 0
        visited[0] = True #base case
        count = 1 #while visiting first room the count is initilised to 1

        while stack:
            room = stack.pop()

            for key in rooms[room]:
                if not visited[key]: #visit room onli if it is unvisited
                    visited[key] = True
                    count += 1
                    stack.append(key)
        
        return count == n #if all rooms visited then true else false is returned here