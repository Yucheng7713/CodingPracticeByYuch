def solution(beginWord, endWord, wordList):
    if endWord not in wordList:
        return 0

    wordList.sort()
    target = wordList.index(endWord)
    path_len = 0
    result = 601
    found = False

    for i in range(len(wordList)):
        if oneDistance(beginWord, wordList[i]):
            found = True
            path_len = 1
            dir = 1 if target - i > 0 else -1
            for j in range(i, target, dir):
                if oneDistance(wordList[j], wordList[j + dir]):
                    path_len += 1
                else:
                    found = False
                    break
            if found: result = min(result, path_len)

    return result + 1 if result < 601 else 0


def oneDistance(str_1, str_2):
    diff_count = 0
    for i in range(len(str_1)):
        if str_1[i] != str_2[i]:
            diff_count += 1
            if diff_count > 1:
                return False
    return diff_count == 1

b_word = "kiss"
e_word = "tusk"
s_list = ["miss",
 "dusk",
 "kiss",
 "musk",
 "tusk",
 "diss",
 "disk",
 "sang",
 "ties",
 "muss"]
s = solution(b_word, e_word, s_list)
print(s)
