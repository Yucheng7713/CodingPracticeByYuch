# Given two strings, write a method to decide if one is a permutation of the other.
# The definition of permutation :
#   1. Both strings have the same length -> the most intuitive condition
#   2. Each character in a given string exists in the other string with the same number of occurences.


# Method 1. Sort both strings and check whether they are the same
# Time complexity : O(nlogn)
# Space complexity : O(1)
def checkPermutation_I(str_1, str_2):
    if len(str_1) != len(str_2):
        return False
    return sorted(str_1) == sorted(str_2)

# Method 2. Use a hash map to keep track of all characters with their occurences and later traverse the other string
#           and check whether each character exists in the hash map with the same occurence.
# Time complexity : O(n)
# Space complexity : O(n)
def checkPermutation_II(str_1, str_2):
    from collections import Counter
    if len(str_1) != len(str_2):
        return False
    counter_1 = Counter(list(str_1))
    for c in str_2:
        if c not in counter_1:
            return False
        else:
            counter_1[c] -= 1
    return all(v == 0 for v in counter_1.values())



if __name__ == '__main__':
    print(checkPermutation_II("acbap", "pabac"))





