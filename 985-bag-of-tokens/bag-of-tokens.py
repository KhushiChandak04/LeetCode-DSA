class Solution(object):
    def bagOfTokensScore(self, tokens, power):
        """
        :type tokens: List[int]
        :type power: int
        :rtype: int
        """
        tokens.sort()
        left = 0 #initialise ptrs
        right = len(tokens) -1
        score = 0 #initialise score to 0
        max_score = 0 #highest achievable score

        while left <= right:

            #can afford the smallest token to increment score
            if power >= tokens[left]:
                power -= tokens[left] #new power value
                score += 1
                max_score = max(max_score, score)
                left += 1
            elif score > 0: #sell of tokens to need power
                power += tokens[right] #add right most token val to retrieve back power
                score -= 1
                right -= 1
            else: #no more possibilities TLE
                break
        return max_score