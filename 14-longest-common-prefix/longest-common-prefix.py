class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = ""
        for i in range(len(strs[0])):
            for s in strs:
                if i >= len(s) or s[i] != strs[0][i]: #no commonality here
                    return prefix

            prefix += strs[0][i]
        return prefix