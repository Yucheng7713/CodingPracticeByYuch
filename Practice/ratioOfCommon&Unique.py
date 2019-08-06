from collections import Counter

def ratioOfCommonAndUnique(str_1: str, str_2: str):
    counter_1 = Counter(list(str_1))
    counter_2 = Counter(list(str_2))

    numOfUnique = len(set(list(str_1) + list(str_2)))
    numOfCommon = 0
    for word in counter_1:
        if word in counter_2:
            numOfCommon += min(counter_1[word], counter_2[word])

    return numOfCommon / numOfUnique

str1 = "ABC"
str2 = "AAD"
print(ratioOfCommonAndUnique(str1, str2))