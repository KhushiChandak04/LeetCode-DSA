class Solution(object):
    def maxNumberOfFamilies(self, n, reservedSeats):
        """
        :type n: int
        :type reservedSeats: List[List[int]]
        :rtype: int
        """
        rows = {}
        for row, seat in reservedSeats:
            if row not in rows:
                rows[row] = [] #if row not in dictionary, create an empty list for it
            rows[row].append(seat) #add reserved seat to that row

        answer = (n-len(rows)) *2 #every fully empty row can fit 2 grps

        for seats in rows.values(): #check only the seats with reserved values
            left = True #check if 2,3,4,5 are free
            if 2 in seats or 3 in seats or 4 in seats or 5 in seats:
                left = False
            middle = True #check if 4,5,6,7 are free
            if 4 in seats or 5 in seats or 6 in seats or 7 in seats:
                middle = False
            right = True #check if 6,7,8,9 are free
            if 6 in seats or 7 in seats or 8 in seats or 9 in seats:
                right = False
            
            if left and right:
                answer += 2 #if both left and right are there then 2 grps can be added

            elif left or right or middle:
                answer += 1 #only one grp can be fitted here
        return answer