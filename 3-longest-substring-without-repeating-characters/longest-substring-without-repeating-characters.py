class Solution(object):
    def lengthOfLongestSubstring(self, s):
        lastseen = {} #creates a hashmap
        left = 0 #initialise ptr
        maxlen = 0 #initialise length as 0

        for right in range(len(s)): #traversal
            if s[right] in lastseen: #duplicate found
                left = max(left, lastseen[s[right]] + 1)
            lastseen[s[right]] = right #store latest position
            maxlen = max(maxlen, right - left + 1) #size of longest substring
        return maxlen