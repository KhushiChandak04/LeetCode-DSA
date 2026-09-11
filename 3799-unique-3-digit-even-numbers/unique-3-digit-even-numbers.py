class Solution(object):
    def totalNumbers(self, digits):
        """
        :type digits: List[int]
        :rtype: int
        """
        #last digit must be even and available in set
        answer = set()

        for a in digits:
            for b in digits:
                for c in digits:

                    if a == 0:
                        continue #3 digit nimber cannot start with 0
                    if c % 2 != 0: #odd last digit
                        continue
                    
                    if [a,b,c].count(a) > digits.count(a): #do not use same copy of digits twice
                        continue
                    if [a,b,c].count(b) > digits.count(b):
                        continue
                    if [a,b,c].count(c) > digits.count(c):
                        continue
                    answer.add(a*100 + b*10 + c)
        return len(answer)