class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        count = {}

        for ch in magazine: #count evry letter in magazine
            if ch in count:
                count[ch] += 1
            else:
                count[ch] = 1
        
        #check evry letter in ransom note
        for ch in ransomNote:
            if ch not in count or count[ch] == 0:
                return False
            else:
                count[ch] -= 1
                
        return True