class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        original_colour = image[sr][sc]
        if color == original_colour: 
            return image #nothing needs to be changed

        rows = len(image)
        cols = len(image[0])

        def dfs(r,c):
            if r < 0 or r >= rows or c < 0 or c >= cols: #border cases
                return
            if image[r][c] != original_colour:
                return #onli change the pixels with original colours

            image[r][c] = color

            dfs(r-1, c) #move up
            dfs(r+1, c) #move down
            dfs(r, c-1) #move left
            dfs(r, c+1) #move right

        dfs(sr,sc)
        return image