class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        arr = [] #stores pts and distances

        for point in points:
            x = point[0]
            y = point[1]

            dist = x*x + y*y #squared dist frm origin
            arr.append([dist, x,y])
        arr.sort()
        ans = [] #store k closet pts

        for i in range(k):
            ans.append([arr[i][1], arr[i][2]])
        return ans