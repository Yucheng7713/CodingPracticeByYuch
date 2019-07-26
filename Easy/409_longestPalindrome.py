class Solution:
    def longestPalindrome(self, s):
        max_length = 0
        p_hash = dict()
        for c in s:
            p_hash[c] = p_hash.get(c, 0) + 1
        for key, value in p_hash.items():
            if value % 2 == 0:
                max_length += value
                p_hash[key] = 0
            elif value % 2 == 1 and value > 2:
                max_length += (value // 2 * 2)
                p_hash[key] = 1
        if any(p_hash.values()):
            max_length += 1
        return max_length

    def longestPalindrome_II(self, s: str) -> int:
        letter_count = collections.Counter(s)
        p_length = add = 0
        for letter, count in letter_count.items():
            if count % 2 == 1:
                add = count - 1
            else:
                add = count
            p_length += add
            letter_count[letter] -= add
        return p_length + 1 if any(letter_count.values()) else p_length

    def longestPalindrome_III(self, s: str) -> int:
        numOfOdd = sum([count & 1 for count in collections.Counter(s).values()])
        return len(s) - numOfOdd + bool(numOfOdd)

palinStr = "civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth"
print(len(palinStr))
s = Solution()
print(s.longestPalindrome(palinStr))