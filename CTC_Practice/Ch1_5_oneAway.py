# There are 3 types of edits that can be performed on strings :
# insert a character, remove a character, or replace a character.
# Given 2 strings, write a function to check if they are one edit (or zero edits) away

# Same problem on Leetcode : #161 One Edit Distance

# Time complexity : O(s1)
# Space complexity : O(s1)

def oneAway(s1, s2):
    if s1 == s2:
        return True
    else:
        diff = abs(len(s1) - len(s2))
        if diff > 1:
            return False
        elif diff == 0:
            # Check replacement
            d = 0
            for i in range(len(s1)):
                if s1[i] == s2[i]: continue
                d += 1
            return d == 1
        else:
            # Check insertion/deletion
            # Enforce to just check for deletion case by swapping s1, s2
            # s1 will always be the string longer than s2 by 1
            if len(s1) < len(s2):
                s1, s2 = s2, s1
            for i in range(len(s1)):
                d_str = s1[:i] + s1[i+1:]
                if d_str == s2:
                    return True
            return False

if __name__ == "__main__":
    a, b = "abcc", "acc"
    print(oneAway(a, b))