# Class for Trie's node
class TrieNode:
    def __init__(self):
        self.links = collections.defaultdict(TrieNode)
        self.isEnd = False

class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word: 'str') -> 'None':
        """
        Inserts a word into the trie.
        """
        temp = self.root
        for ch in word:
            temp = temp.links[ch]
        temp.isEnd = True

    def search(self, word: 'str') -> 'bool':
        """
        Returns if the word is in the trie.
        """
        temp = self.root
        for ch in word:
            if ch not in temp.links:
                return False
            temp = temp.links[ch]
        return temp.isEnd

    def startsWith(self, prefix: 'str') -> 'bool':
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        temp = self.root
        for ch in prefix:
            if ch not in temp.links:
                return False
            temp = temp.links[ch]
        return True

        # Your Trie object will be instantiated and called as such:
        # obj = Trie()
        # obj.insert(word)
        # param_2 = obj.search(word)
        # param_3 = obj.startsWith(prefix)