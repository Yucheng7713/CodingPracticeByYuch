# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        start, end = 0, n
        while start < end:
            mid = (start + end) // 2
            if isBadVersion(mid):
                if not isBadVersion(mid - 1):
                    return mid
                end = mid - 1
            else:
                if isBadVersion(mid + 1):
                    return mid + 1
                start = mid + 1
        return -1