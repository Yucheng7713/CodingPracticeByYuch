# Given a string, write a function to check if it is a permutation of a palindrome.
# The definition of palindrome : a word or phrase that is the same forwards and backwards.
# There are two types of palindrome :
#   1. bab
#   2. baab
# Notice the number of occurences of each character, each character appears even number of times.
# Only at most one character is allowed to appear odd number of times
# If there are more than one character appear odd number of times, then there is no way for this string to
# form a palindrome.

# Therefore, we just need to check the number of occurences of each character.
# if there appears no odd occurences character or only one odd occurences character, then return True.

# Time complexity : O(n)
# Space complexity : O(n)

def palindromePermutation(str):
    from collections import Counter
    p_str = str.lower().replace(" ", "")
    p_counter = Counter(list(p_str))
    n = 0
    for v in p_counter.values():
        if v % 2 == 1:
            n += 1
    return n == 0 or n == 1

if __name__ == "__main__":
    str = "aab"
    print(palindromePermutation(str))

