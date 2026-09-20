class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        answer = ""
        word = ""

        #start from last character
        for i in range(len(s) -1, -1, -1):
            if s[i] != ' ': #if no space, then add it to the word
                word = s[i] + word
            #if we reach a space, its a word
            elif word != '':
                if answer != '':
                    answer += ' '
                answer += word
                word = ""
        
        #add the last word
        if word != "":
            if answer != "":
                answer += " "
            answer += word
        return answer