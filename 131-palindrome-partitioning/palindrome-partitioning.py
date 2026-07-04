class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        answer = []
        current = []

        def ispalindrome(string):
            return string == string[::-1] #string equal to its reverse

        def backtrack(start):
            if start == len(s): #if entire string has been partitioned
                answer.append(current[:])
                return
            for end in range(start, len(s)):
                substring = s[start:end + 1]
                
                if ispalindrome(substring):
                    current.append(substring)
                    backtrack(end + 1)
                    current.pop()
        backtrack(0)
        return answer