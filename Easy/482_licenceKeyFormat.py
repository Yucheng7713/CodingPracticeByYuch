class Solution:
    def licenseKeyFormatting(self, S, K):
        licenseKey = ""
        S = S.upper().replace("-", "")
        for i in range(0, len(S), K):
            licenseKey = "-" + S[-K:] + licenseKey
            S = S[:-K]
        if len(S) > 0:
            return S + licenseKey
        return licenseKey[1:]

s = Solution()
S = "2-5g-3-J"
K = 4

print(s.licenseKeyFormatting(S, K))
