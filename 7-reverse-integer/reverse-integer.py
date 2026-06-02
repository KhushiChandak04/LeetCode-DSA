class Solution(object):
    def reverse(self, x):
        sign = -1 if x < 0 else 1
        x = abs(x) #mods the absolute value
        revNum = 0 #varibale to store reversed number

        while x > 0:
            lastdigit = x % 10 #modular div gives last digit if by 10
            revNum = revNum * 10 + lastdigit #append to reversed
            x = x // 10 #removes last digit from the number once it is appended to new place
        revNum = sign * revNum

        if revNum < -(2**31) or revNum > (2**31 - 1): #for exceeding size
            return 0
        return revNum