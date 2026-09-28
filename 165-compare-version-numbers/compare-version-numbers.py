class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        a = version1.split(".") #split at .
        b = version2.split(".")

        #find larger number of revisions
        n = max(len(a), len(b))

        #compare every revision
        for i in range(n):
            if i < len(a):
                x = int(a[i]) #here take revison version1
            else:
                x = 0
            if i < len(b):
                y = int(b[i])
            else:
                y = 0
            
            if x < y:
                return -1
            if x > y:
                return 1

        return 0 #if all revisions are equal