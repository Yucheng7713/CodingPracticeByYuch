class Solution:
    def isAnagram(self, s, t):
        myMap = dict()
        for l in s:
            myMap[l] = myMap.get(l, 0) + 1
        for k in t:
            if k not in myMap.keys():
                return False
            else:
                myMap[k] -= 1
        return all(x == 0 for x in myMap.values())


    def isAnagram_II(self, s, t):
        myMap = {}
        for l in s:
            if l not in myMap:
                myMap[l] = 1
            else:
                myMap[l] += 1

        for k in t:
            if k not in myMap:
                return False
            else:
                myMap[k] -= 1

        for v in myMap.values():
            if v != 0:
                return False
        return True

s = Solution()
print(s.isAnagram("ab", "a"))