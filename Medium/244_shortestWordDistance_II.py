class WordDistance:
    # Initialize a hash map with :
    # 'word' : [index_1, index_2, index_3....]
    def __init__(self, words: 'List[str]'):
        self.word_dict = collections.defaultdict(list)
        for i, word in enumerate(words):
            self.word_dict[word] += [i]

    def shortest(self, word1: 'str', word2: 'str') -> 'int':
        word1_indexes = self.word_dict[word1]
        word2_indexes = self.word_dict[word2]
        i = j = 0
        min_diff = float('inf')
        while i < len(word1_indexes) and j < len(word2_indexes):
            min_diff = min(min_diff, abs(word1_indexes[i] - word2_indexes[j]))
            if word1_indexes[i] < word2_indexes[j]:
                # Moving i index
                i += 1
            else:
                # Moving j index
                j += 1
        return min_diff

        # Your WordDistance object will be instantiated and called as such:
        # obj = WordDistance(words)
        # param_1 = obj.shortest(word1,word2)


        # Your WordDistance object will be instantiated and called as such:
        # obj = WordDistance(words)
        # param_1 = obj.shortest(word1,word2)