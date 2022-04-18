class Solution:
    # Method 1 : Two pointers

    def compress_I(self, chars):
        s_index = f_index = anchor = count = 0
        c_chars = chars[0]
        while s_index < len(chars):
            if (f_index == len(chars)):
                if count > 1:
                    c_chars += str(count)
                    chars[anchor:anchor + len(c_chars)] = c_chars
                    anchor += len(c_chars)
                else:
                    chars[anchor:anchor + len(c_chars)] = c_chars
                    anchor += 1
                break
            elif chars[s_index] != chars[f_index]:
                if count > 1:
                    c_chars += str(count)
                    chars[anchor:anchor + len(c_chars)] = c_chars
                    anchor += len(c_chars)
                else:
                    chars[anchor:anchor + len(c_chars)] = c_chars
                    anchor += 1
                s_index = f_index
                c_chars = chars[f_index]
                count = 1
            else:
                count += 1
            f_index += 1
        return anchor

    def compress_II(self, chars: List[str]) -> int:
        s = f = anchor = count = 0
        for f in range(len(chars) + 1):
            if f < len(chars) and chars[s] == chars[f]:
                count += 1
            else:
                chars[anchor] = chars[s]
                anchor += 1
                if count > 1:
                    s_count = str(count)
                    for j in range(len(s_count)):
                        chars[anchor] = s_count[j]
                        anchor += 1
                s = f
                count = 1
        return anchor

s = Solution()
cs = ["a","a","a","a","b","a"]
print(s.compress(cs))
print(cs)