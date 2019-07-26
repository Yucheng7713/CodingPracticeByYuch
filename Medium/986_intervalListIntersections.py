# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    def intervalIntersection(self, A: List[Interval], B: List[Interval]) -> List[Interval]:
        a_index = b_index = 0
        results = []
        while a_index < len(A) and b_index < len(B):
            # If Interval exists
            if A[a_index].end >= B[b_index].start and B[b_index].end >= A[a_index].start:
                new_inter = Interval()
                if B[b_index].start <= A[a_index].start:
                    new_inter.start = A[a_index].start
                else:
                    new_inter.start = B[b_index].start
                if B[b_index].end <= A[a_index].end:
                    new_inter.end = B[b_index].end
                    b_index += 1
                else:
                    new_inter.end = A[a_index].end
                    a_index += 1
                results.append(new_inter)
            # If interval doesn't exist
            # 想出辦法來移動 two pointers
            # 不能用 pointer 本身的大小來決定移動與否 -> 須看當前哪個 interval 超前來做判斷
            else:
                if B[b_index].start > A[a_index].end:
                    a_index += 1
                elif A[a_index].start > B[b_index].end:
                    b_index += 1
        return results

    def intervalIntersection_II(self, A: List[Interval], B: List[Interval]) -> List[Interval]:
        i = j = 0
        results = []
        while i < len(A) and j < len(B):
            if A[i].end < B[j].start:
                i += 1
            elif B[j].end < A[i].start:
                j += 1
            else:
                results.append(Interval(max(A[i].start, B[j].start), min(A[i].end, B[j].end)))
                if B[j].end < A[i].end:
                    j += 1
                else:
                    i += 1
        return results


