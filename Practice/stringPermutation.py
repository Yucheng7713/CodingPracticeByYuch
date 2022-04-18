

def stringPermutation(p_str):
    def permutation(prefix, remain):
        if not remain:
            print(prefix)
        for i in range(len(remain)):
            permutation(prefix + remain[i], remain[:i] + remain[i+1:])
    permutation("", p_str)

p_str = "abc"
stringPermutation(p_str)