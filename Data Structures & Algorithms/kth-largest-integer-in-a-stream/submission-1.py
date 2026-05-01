from typing import List


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        heap = [i for i in nums]
        if len(heap) >= k:
            self.heap = heapq.nlargest(k ,heap)
        else:
            self.heap = heap
        heapq.heapify(self.heap)
        

    def add(self, val: int) -> int:
        #store as neg value
        # print(f"adding val: {val}")
        # print(f"heap: {self.heap}")
        if len(self.heap) < self.k:
            heapq.heappush(self.heap,val)
            out = self.heap[0]
        else:
            out = heapq.heappushpop(self.heap, val)
        # print(f"out: {out}")
        return  self.heap[0]
        
