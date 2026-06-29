class Solution(object):
    def minNumberOfFrogs(self, croakOfFrogs):
        """
        :type croakOfFrogs: str
        :rtype: int
        """
        c = r = o = a = 0
        active_frogs = 0
        max_frogs = 0
        for ch in croakOfFrogs:
            if ch == 'c':
                c += 1
                active_frogs += 1
                max_frogs = max(max_frogs, active_frogs)

            elif ch == 'r': #frog moves from c -> r
                if c == 0:
                    return -1 #no frogs to move ahead
                c -= 1
                r += 1
            elif ch == 'o': #frog moves from r -> o
                if r == 0:
                    return -1 #cant move ahead
                r -= 1
                o += 1
            elif ch == 'a':
                if o == 0:
                    return -1
                o -= 1
                a += 1
            elif ch == 'k':
                if a == 0:
                    return -1
                a -= 1
                active_frogs -= 1
                
        #if any frog did not finish fully then
        if c or r or o or a:
            return -1
        return max_frogs