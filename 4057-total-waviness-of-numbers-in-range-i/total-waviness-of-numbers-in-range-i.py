class Solution(object):
    def totalWaviness(self, num1, num2):
        total = 0 #initialise
        for num in range (num1, num2 + 1):
            s = str(num) #convert to string to compare
            if len(s) < 3: #len less than 3
                continue
            waviness = 0 #initialise
            for i in range (1, len(s)-1):
                #peak
                if s[i] > s[i-1] and s[i] > s[i+1]:
                    waviness += 1
                #valley
                elif s[i] < s[i-1] and s[i] < s[i+1]:
                    waviness +=1
            total += waviness
        return total