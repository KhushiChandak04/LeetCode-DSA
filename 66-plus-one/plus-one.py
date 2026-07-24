class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        #simple carry propagation problem
        for i in range(len(digits) -1, -1, -1): #traverse from last digit
            if digits[i] < 9:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0 #if digit is 9, make it 0 and carry
        return [1] + digits #if all digits are 9