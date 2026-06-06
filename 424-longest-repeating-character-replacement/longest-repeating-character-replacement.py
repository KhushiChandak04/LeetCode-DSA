class Solution(object):
    def characterReplacement(self, s, k):
        count = {} #hash initialise
        left = 0 #ptr
        max_freq = 0
        ans = 0 
        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1 #stores count of each alphabet
            max_freq = max(max_freq, count[s[right]])
            #invalid window
            while (right - left + 1) - max_freq > k:
            #formula is lenght of substring - max_freq = k
                count[s[left]] -= 1
                left += 1
            ans = max(ans, right - left + 1)
        return ans