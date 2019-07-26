class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_map = dict()
        for i, l in enumerate(order):
            order_map[l] = i
        for j in range(len(words) - 1):
            first_word, second_word = words[j], words[j+1]
            s_prefix = True
            for k in range(min(len(first_word), len(second_word))):
                if order_map[first_word[k]] < order_map[second_word[k]]:
                    s_prefix = False
                    break
                elif order_map[first_word[k]] > order_map[second_word[k]]:
                    return False
            if s_prefix and len(first_word) > len(second_word):
                return False
        return True