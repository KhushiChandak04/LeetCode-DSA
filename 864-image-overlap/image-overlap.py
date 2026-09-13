class Solution(object):
    def largestOverlap(self, img1, img2):
        """
        :type img1: List[List[int]]
        :type img2: List[List[int]]
        :rtype: int
        """
        points1 = []
        points2 = []

        for i in range(len(img1)): #store 1s in the grid for img1
            for j in range(len(img1)):
                if img1[i][j] == 1:
                    points1.append((i,j))

        for i in range(len(img2)): #stores 1s in the grid for img2
            for j in range(len(img2)):
                if img2[i][j] == 1:
                    points2.append((i,j))
        
        shifts = {} #try matching

        for x1, y1 in points1:
            for x2,y2 in points2:
                shift = (x2-x1, y2-y1)

                if shift not in shifts:
                    shifts[shift] = 0

                shifts[shift] += 1

        if len(shifts) == 0: #no element in shifts, most common shift -> maximum overlap
            return 0
        return max(shifts.values())