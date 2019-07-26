import heapq

class KthLargest:
    # Keep a fixed k size min heap to keep the top ( minimum ) as the k-th largest element
    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)
        # Get rid of the elements smaller than k-th largest element
        # Those elements won't affect the result
        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        # If the answer is changed
        elif val > self.heap[0]:
            # Pop the old k-th largest element and insert the new val
            # After heapify, return the new k-th largest element
            heapq.heapreplace(self.heap, val)
        return self.heap[0]




        # Your KthLargest object will be instantiated and called as such:
        # obj = KthLargest(k, nums)
        # param_1 = obj.add(val)

obj = KthLargest(3, [4,5,8,2])
print(obj.add(3))
print(obj.add(5))
print(obj.add(10))
print(obj.add(9))
print(obj.add(4))