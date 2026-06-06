class Solution(object):
    def groupAnagrams(self, strs):
        groups = {} #key = sorted word, value = list of anagrams
        for word in strs:
            key = "".join(sorted(word)) #all anagrams give same sorted word
            if key not in groups:
                groups[key] = [] #create new group if not present
            groups[key].append(word) #add current word into its group
        return groups.values()