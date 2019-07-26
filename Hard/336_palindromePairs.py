class Solution:
    # Brute Force - Check out all possible pairs
    # Time complexity : O(n^2k)
    # Space complexity : O(n)
    def palindromePairs_I(self, words):
        def checkPalindromic(word):
            mid = len(word) // 2
            right = mid
            left = mid if len(word) % 2 == 1 else mid - 1
            N = mid if len(word) % 2 == 1 else mid - 1
            for i in range(N+1):
                if word[right] != word[left]:
                    return False
                left, right = left - 1, right + 1
            return True
            # return word == word[::-1]

        results = []
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if checkPalindromic(words[i] + words[j]):
                    results += [[i, j]]
                if checkPalindromic(words[j] + words[i]):
                    results += [[j, i]]

        return results

    # Find the other half palindrome - Low performance
    # Time complexity : O(nk^2)
    # Space complexity : O(n)
    def palindromePairs_II(self, words):
        def checkPalindromic(word):
            return word == word[::-1]
        results = []
        p_map = {}
        for i, word in enumerate(words):
            p_map[word] = i
        for i, word in enumerate(words):
            n = len(word)
            for j in range(n + 1):
                prefix = word[:j]
                suffix = word[j:]
                if checkPalindromic(prefix):
                    left_half = suffix[::-1]
                    # The time complexity could increase tremendously if one uses "left_half in words"
                    if left_half in p_map and left_half != word:
                        results.append([p_map[left_half], i])
                if j != n and checkPalindromic(suffix):
                    right_half = prefix[::-1]
                    if right_half in p_map and right_half != word:
                        results.append([i, p_map[right_half]])
        return results

    # Use Trie
    def palindromePairs_III(self, words):


words = ["abcd","dcba","lls","s","sssll"]
words_II = ["a", ""]
print(Solution().palindromePairs_II(words_II))