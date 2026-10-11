class Solution(object):
    def maximumGain(self, s, x, y):
        """
        :type s: str
        :type x: int
        :type y: int
        :rtype: int
        """
        def remove(s, first, second, points): #make a function to remove pair and calculate pts
            stack = []
            score = 0

            for ch in s:
                #check if they form curr pair or no?
                if stack and stack[-1] == first and ch == second:
                    stack.pop()
                    score += points
                else:
                    stack.append(ch)

            return stack, score

        if x >= y: #remove the pair with higher points first
            s, score1 = remove(s, 'a', 'b', x)
            s, score2 = remove(s, 'b', 'a', y)
        else:
            s, score1 = remove(s, 'b', 'a', y)
            s, score2 = remove(s, 'a', 'b', x)
        
        return score1 + score2