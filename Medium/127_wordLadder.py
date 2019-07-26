import collections

class Solution:
    # Preconstruct an adjacent hash map for quick accessing all adjacent ( 1 edit distance )
    # words in constant time
    def constructAdjacentMap(self, words):
        adj_map = dict()
        for word in words:
            for i in range(len(word)):
                s = word[:i] + "_" + word[i + 1:]
                adj_map[s] = adj_map.get(s, []) + [word]
        return adj_map

    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if endWord not in wordList:
            return 0
        adjMap = self.constructAdjacentMap(wordList)
        w_queue, visited = collections.deque([(beginWord, 1)]), set()
        while w_queue:
            word, edit_distance = w_queue.popleft()
            if word not in visited:
                visited.add(word)
                if word == endWord:
                    return edit_distance
                for i in range(len(word)):
                    adj_words = adjMap.get(word[:i] + "_" + word[i + 1:], [])
                    for adj in adj_words:
                        if adj not in visited:
                            w_queue.append([(adj, edit_distance + 1)])
        return 0

    def ladderLength_II(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # Preconstruct an adjacent hash map for quick accessing all adjacent ( 1 edit distance )
        # words in constant time
        edit_map = collections.defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                s = word[:i] + '_' + word[i+1:]
                edit_map[s] += [word]
        # BFS search until we find the end word -> return the shortest edit distance
        queue = [beginWord]
        edit_distance = 1
        visited = set()
        while queue:
            q_len = len(queue)
            for k in range(q_len):
                w = queue.pop(0)
                # If the word popped from the queue hasn't been visited
                if w not in visited:
                    visited.add(w)
                    # Find all its neighbors ( which only has 1 edit distance to it )
                    # and append those hasn't been visited into the queue
                    for i in range(len(w)):
                        for adj in edit_map[w[:i] + '_' + w[i+1:]]:
                            if adj not in visited:
                                queue += [adj]
            # Increase the edit distance
            edit_distance += 1
            if endWord in queue: return edit_distance
        return 0

b_word = "lost"
e_word = "miss"
words = ["most","mist","miss","lost","fist","fish"]
print(Solution().ladderLength(b_word, e_word, words))