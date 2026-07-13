class Solution(object):
    def sequentialDigits(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: List[int]
        """
        #onli 36 seq nos possible from 1 to 123456789
        digits = "123456789" #make it a string
        answer = []
        for i in range(2,10): #length of number
            for start in range(0, 10-i): #start position
                number = int(digits[start: start+i])
                if low <= number <= high:
                    answer.append(number)
        return answer