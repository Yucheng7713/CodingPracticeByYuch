from collections import Counter


def solution(a):
    c = Counter()
    result = []
    for n in range(len(a)):
        for d in str(a[n]):
            c[d] += 1
    max_count = max(c.values())

    for digit in c.keys():
        if c[digit] == max_count:
            result += [int(digit)]

    return result


a = [25, 2, 3, 57, 38, 41]
s = solution(a)
print(s)