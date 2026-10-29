class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        m = len(mat)
        n = len(mat[0])

        dist = [[-1]*n for i in range(m)] #create a dist matrix with -1 = not visited
        q = deque() #initilise a double ended queue here

        #distance of all zeroes from nearest 0 is alrd 0
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    dist[i][j] = 0
                    q.append((i,j))
        
        #check all 4 directions
        directions = [(1,0), (0,1), (-1,0), (0,-1)]

        while q:
            r,c = q.popleft() #process all items addded to deque one by one

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                #check boundary conditions
                if nr >= 0 and nr < m and nc >= 0 and nc < n:
                    if dist[nr][nc] == -1: #neighbour not visited
                        dist[nr][nc] = dist[r][c] + 1 #dist is 1 more than curr cell
                        q.append((nr,nc)) #add neighbour to queue to chk its elements
        return dist