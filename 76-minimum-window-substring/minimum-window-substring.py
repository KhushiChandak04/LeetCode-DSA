class Solution(object):
    def minWindow(self, s, t):

        targetcount = {} #stores freq for target
        for ch in t:
            targetcount[ch] = targetcount.get(ch,0) + 1
        window_count = {}
        matched_chars = 0 #currently how many matched so far
        left = 0 #left ptr
        minLen = float('inf')
        start = 0

        for right in range(len(s)):
            window_count[s[right]] = window_count.get(s[right],0) + 1
            if s[right] in targetcount and window_count[s[right]] <= targetcount[s[right]]:
                matched_chars += 1
            while matched_chars == len(t):
                if right-left+1 < minLen:
                    minLen = right-left+1
                    start = left

                #before removing left char check if it is contributing

                if s[left] in targetcount and window_count[s[left]] <= targetcount[s[left]]:
                    matched_chars -= 1
                window_count[s[left]] -= 1
                left += 1
        if minLen == float('inf'):
            return ""
        return s[start:start+minLen]