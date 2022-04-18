# Implement a method to perform basic string compression using the counts of repeated characters.
# For instance, a string aabcccccaaa would become a2b1c5a3.
# If the "compressed" string would not become smaller than the original string, your method should
# return the original string.
# You may assume the string has only uppercase and lowercase letters.

# Similar problem : Leetcode #443 String Compression

def stringCompression(s):
    if not s: return s
    compressed_str = ""
    prev_char = s[0]
    count = 0
    for c in s:
        if c == prev_char:
            count += 1
        else:
            compressed_str += prev_char + str(count)
            count = 1
        prev_char = c
    compressed_str += prev_char + str(count)
    return compressed_str if len(compressed_str) < len(s) else s


if __name__ == "__main__":
    s1 = "aabcccccaaa"
    s2 = "acbbbbbbbba"
    s3 = ""
    print(stringCompression(s3))