class Solution:
    def search_helper(self, nums, target, start, end):
        print(f"end - start: {end - start}")
        # print(f"start: {start}, end: {end}")

        if end - start == 0 :
            if target == nums[start]:
                return start
            else: return -1
        if end - start == 1:
            # print(f"checking for diff of 1")
            if target == nums[start]:
                return start
            elif target == nums[end]:
                return end
            else: return -1
        # if end-start == 2:
        #     if target == nums[0]:
        #         return start
        #     elif target == nums[1]:
        #         return start
        #     else: return -1
            
        # else longer than 1 
        bisect = (start + end)//2
        if target > nums[bisect]:
            return self.search_helper(nums, target, bisect, end)
        elif target < nums[bisect]:
            return self.search_helper(nums, target, start, bisect)
        else: # target == bisect then return bisect index:
            return bisect

            
    def search(self, nums: List[int], target: int) -> int:
        return self.search_helper(nums, target, 0, len(nums) - 1) 
        
