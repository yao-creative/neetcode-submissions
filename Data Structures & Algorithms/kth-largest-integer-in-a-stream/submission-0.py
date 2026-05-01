from typing import List


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = [-i for i in nums]
        heapq.heapify(self.heap)

    def add(self, val: int) -> int:
        #store as neg value
        # print(f"val: {val}")
        heapq.heappush(self.heap, -val)
        # check the  - smallest k ~ largest k
        smallest = heapq.nsmallest(self.k, self.heap)
        # print(f"smallest list: {heapq.nsmallest(self.k, self.heap)}")
        
        return - smallest[-1]


