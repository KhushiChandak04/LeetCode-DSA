class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return
        
        phone = { #stores dictionary mapping
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz"
        }
        ans = []
        def backtrack(i, current): #i = current digit index, and curr = word formed
            if len(current) == len(digits): #base case
                ans.append(current)
                return
            for ch in phone[digits[i]]:
                backtrack(i+1, current + ch) #iterate to next combo
        backtrack(0, "")
        return ans