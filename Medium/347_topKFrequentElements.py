import collections
from heapq import _heappop_max, _heapify_max
from typing import List

class Solution:
    # Method 1 : Push all elements into a hash map then prompt the elements in hash map to a max heap
    # Pop k elements from the heap, the result will be the top kth frequent elements
    def topKFrequent_I(self, nums: List[int], k: int) -> List[int]:
        num_counter = collections.Counter(nums)
        heap, top_k = [], []
        for num, count in num_counter.items():
            heap.append((count, num))
        _heapify_max(heap)
        for i in range(k):
            top_k.append(_heappop_max(heap)[1])
        return top_k

    def topKFrequent_II(self, nums: List[int], k: int) -> List[int]:
        num_counter = collections.Counter(nums)
        heap, top_k = [], []
        # Push elements into the heap
        for num, count in num_counter.items():
            heappush(heap, (count, num))
            # If the current number of elements exceed k, then we can pop the minimum elements out
            if len(heap) > k:
                heappop(heap)
        # The rest k elements will be the top k frequent elements
        # !! But be aware of the order, need to reverse it.
        return [n[1] for n in heap[::-1]]

    # Method 2 : Sort the hashmap then output the first k elements
    def topKFrequent_III(self, nums: List[int], k: int) -> List[int]:
        num_counter = collections.Counter(nums)
        return [n[0] for n in sorted(list(num_counter.items()), key=lambda x:x[1], reverse=True)][:k]

nums = [1,1,1,2,2,3]
k = 2
print(Solution().topKFrequent_I(nums, k))