class Solution:
    def groupAnagrams(self, strs):
        anagrams = dict()
        output = []
        for str in strs:
            anagrams[''.join(sorted(str))] = anagrams.get(''.join(sorted(str)), []) + [str]
        for k, v in anagrams.items():
            output.append(v)
        return output

    def groupAnagrams_II(self, strs):
        anagrams = dict()
        output = []
        for str in strs:
            anagrams[tuple(sorted(str))] = anagrams.get(tuple(sorted(str)), []) + [str]
        for k, v in anagrams.items():
            output.append(v)
        return output