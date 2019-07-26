import collections

class dictNode:
    def __init__(self):
        self.word_dict = collections.defaultdict(dictNode)
        self.isWord = False
        self.isEnd = False

class WordDictionary:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = dictNode()

    def addWord(self, word: 'str') -> 'None':
        """
        Adds a word into the data structure.
        """
        temp = self.root
        for ch in word:
            temp = temp.word_dict[ch]
            temp.isEnd = False
        temp.isEnd = True
        temp.isWord = True

    def search(self, word: 'str') -> 'bool':
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """

        def backTracking(word, node):
            if not word:
                return node.isWord
            if len(word) > 0 and node.isEnd:
                return False
            wordMatch = False
            for i in range(len(word)):
                if word[i] == '.':
                    for key, d_node in node.word_dict.items():
                        wordMatch = wordMatch or backTracking(word[i + 1:], d_node)
                        if wordMatch:
                            return wordMatch
                    return False
                else:
                    if word[i] not in node.word_dict:
                        return False
                    else:
                        node = node.word_dict[word[i]]
            return wordMatch or node.isWord

        temp = self.root
        return backTracking(word, temp)

# Your WordDictionary object will be instantiated and called as such:
obj = WordDictionary()
obj.addWord("a")
obj.addWord("ab")
print(obj.search("a"))
print(obj.search("a."))
print(obj.search("ab"))
print(obj.search(".a"))
print(obj.search(".b"))
print(obj.search("ab."))
print(obj.search("."))
print(obj.search(".."))

