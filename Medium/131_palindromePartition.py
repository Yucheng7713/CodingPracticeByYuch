class Solution:
    def backTracking(self, sub_str, path, result):
        if not sub_str:
            result.append(path)
            return
        for i in range(1, len(sub_str) + 1):
            pre, post = sub_str[:i], sub_str[i:]
            if pre == pre[::-1]:
                self.backTracking(post, path + [pre], result)
    def partition(self, s):
        result = []
        self.backTracking(s, [], result)
        return result

s = "aab"
print(Solution().partition(s))