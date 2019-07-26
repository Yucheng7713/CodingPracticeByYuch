class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        i1 = i2 = -1
        min_dist = float('inf')
        for i in range(len(words)):
            if words[i] == word1:
                i1 = i
            elif words[i] == word2:
                i2 = i
            # If both indice get updated, update the current minimum distance
            if i1 >= 0 and i2 >= 0:
                min_dist = min(min_dist, abs(i1 - i2))
        return min_dist

