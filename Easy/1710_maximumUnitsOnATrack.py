def maximumUnits(boxTypes: List[List[int]], truckSize: int) -> int:
    result = 0
    boxTypes.sort(key=lambda x: x[1], reverse=True)

    for i in range(len(boxTypes)):
        if truckSize >= boxTypes[i][0]:
            result += boxTypes[i][0] * boxTypes[i][1]
            truckSize -= boxTypes[i][0]
        else:
            result += truckSize * boxTypes[i][1]
            break

    return result

class Solution:
    pass
