class Solution(object):
    def shortestWordDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        min_dist = float('inf')
        if word1 != word2:
            i1 = i2 = -1
            for i in range(len(words)):
                if words[i] == word1:
                    i1 = i
                elif words[i] == word2:
                    i2 = i
                # If both indice get updated, update the current minimum distance
                if i1 >= 0 and i2 >= 0:
                    min_dist = min(min_dist, abs(i1 - i2))
        else:
            prev_i = -1
            for i in range(len(words)):
                if words[i] == word1:
                    if prev_i >= 0:
                        min_dist = min(min_dist, abs(i - prev_i))
                    prev_i = i
        return min_dist

class Solution_II(object):
    def shortestWordDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        min_dist = float('inf')
        i1 = i2 = -1
        for i in range(len(words)):
            if words[i] == word1:
                i1 = i
            # If word1 == word2, the second condition statement will definitely be
            # true and here we need to a workaround for the case that
            # i2 get updated with i1 with the same index value
            if words[i] == word2:
                # if word1 equals word2, then i1 should be back to the previous index
                # which is also the previous i2
                if word1 == word2:
                    i1 = i2
                # i2 updates as usual
                i2 = i
            # If both indice get updated, update the current minimum distance
            if i1 >= 0 and i2 >= 0:
                min_dist = min(min_dist, abs(i1 - i2))
        return min_dist

