class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        answer = "1" #initial value
        for _ in range(n-1):
            new = ""
            i = 0 #counter

            while i < len(answer):
                count = 1
                #count the same numbers
                while i+1 < len(answer) and answer[i] == answer[i+1]:
                    count += 1
                    i += 1
                new += str(count) + answer[i]
                i += 1
            answer = new
        return answer