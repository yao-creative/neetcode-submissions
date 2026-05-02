from typing import List

class Solution:
    def backtrack(self, i, subset, n, nums):
        if i == n : #iteration including 0 item case to n item case
            return [subset.copy()]
        print(f"i: {i}, subset: {subset}")
        # skip or take (transition states enumerated)/ binary tree fork
        skip = self.backtrack(i+1, subset, n, nums)
        #take
        subset.append(nums[i])
        take = self.backtrack(i+1, subset, n, nums)
        subset.pop() 
        #return all possibilities
        return skip + take

        
        #else choose to include not include item
        
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #this is like recursive splitting pick and no pick. or we can technical join paritions/ filtrations start from [] and single sized. 
        # init is probably []

        return self.backtrack(0, [], len(nums), nums)

        