class Trie(object):
#root = {}
#insert  -> create nested dictionaries
#search  -> path exists AND '*' present
#startsWith -> path exists only

    def __init__(self):
        self.root = {} #initialise an empty dictionary

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        curr = self.root
        for ch in word:
            if ch not in curr:
                curr[ch] = {}
            curr = curr[ch]
        curr["*"] = True #marks end of the word

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        curr = self.root
        for ch in word:
            if ch not in curr:
                return False
            curr = curr[ch]
        return "*" in curr

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        curr = self.root
        for ch in prefix:
            if ch not in curr:
                return False
            curr = curr[ch]
        return True
# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)