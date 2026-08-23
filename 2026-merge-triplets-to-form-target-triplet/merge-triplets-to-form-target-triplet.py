class Solution(object):
    def mergeTriplets(self, triplets, target):
        """
        :type triplets: List[List[int]]
        :type target: List[int]
        :rtype: bool
        """
        x,y,z = target
        a=b=c= False

        for triplet in triplets:
            if triplet[0] > x or triplet[1] > y or triplet[2] > z:
                continue
            a = max(a, triplet[0])
            b = max(b, triplet[1])
            c = max(c, triplet[2])
        return a == x and b == y and c == z