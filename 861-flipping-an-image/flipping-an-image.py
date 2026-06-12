class Solution(object):
    def flipAndInvertImage(self, image):
        """
        :type image: List[List[int]]
        :rtype: List[List[int]]
        """
        n = len(image)
        for i in range(n):
            image[i].reverse() #first reverse each row
        
        for i in range(n):
            for j in range(len(image[0])):
                image[i][j] ^= 1 #xor inverts the bits
        return image