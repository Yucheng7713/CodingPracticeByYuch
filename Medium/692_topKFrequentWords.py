import heapq
import collections

class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        result = []
        word_counts = collections.Counter(words).most_common()
        count_map = collections.defaultdict(list)
        for word, count in word_counts:
            count_map[count] += [word]
        w_list = sorted(count_map.items(), reverse=True)
        while k > 0:
            words = w_list.pop(0)[1]
            words.sort()
            while words and k > 0:
                result += [words.pop(0)]
                k -= 1
        return result

words = ["i", "love", "leetcode", "i", "love", "coding"]
words_2 = ["aaa", "aa", "a"]
words_3 = ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]
k = 4
print(Solution().topKFrequent(words_3, k))