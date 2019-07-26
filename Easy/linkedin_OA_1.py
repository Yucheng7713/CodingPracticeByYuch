def cutSticks(lengths):
    # Write your code here
    lengths.sort()
    result = []
    anchor = cut_offset = 0
    result.append(len(lengths))
    while anchor < len(lengths) - 1:
        cut_offset = lengths[anchor]
        if lengths[anchor] != lengths[anchor + 1]:
            lengths[anchor + 1:] = [k - cut_offset for k in lengths[anchor + 1:]]
            result.append(len([k - cut_offset for k in lengths[anchor + 1:]]))
        anchor += 1

lens = [5, 4, 4, 2, 2, 8]
print(cutSticks(lens))

def getMinimumUniqueSum(arr):
    duplicates = dict()
    min_sum = sum(set(arr))
    for i in range(len(arr)):
        duplicates[arr[i]] = duplicates.get(arr[i], 0) + 1
    for num, time in duplicates.items():
        if time > 1:
            while duplicates.get(num+1, 0) == 0:
                num += 1
            min_sum +=