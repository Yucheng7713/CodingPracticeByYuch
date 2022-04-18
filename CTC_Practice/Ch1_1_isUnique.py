# Determine if a string has all unique characters
# The first question that should be asked is to clarify the format of characters
# is it ASCII or Unicode ?
# If it is ASCII, then it can be easily solved with constant space complexity
# Otherwise extra data storage might be needed. (e.g. set or dict)

def isUnique(str):
    char_array = [True] * 128
    for c in str:
        if char_array[ord(c)]:
            char_array[ord(c)] = False
            continue
        return char_array[ord(c)]
    return True

if __name__ == '__main__':
    s = "1234abc"
    print(isUnique(s))