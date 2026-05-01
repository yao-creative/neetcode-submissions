class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort by start just in case?
        intervals.sort(key=lambda x: x[0])
   
        merged = merged = [intervals[0]]
        for i in range(1,len(intervals)):
            # if i+1 start <= i end then merge, perhaps also keep checking the last one in merge
            # check last one in merge, merge to that else add new one.
            # print(f"merged: {merged} i: {i} intervals i: {intervals[i]}")                
       
            # overlap
            if merged[-1][1] >= intervals[i][0]:
                if merged[-1][1] >= intervals[i][1]: #second one is still encapsulated.
                    continue
                else: #should merge when previous upperbound less than current upperboun
                    merged[-1] = [merged[-1][0], intervals[i][1]]
            else: #no overlap then just append
                merged.append(intervals[i])
                
        return merged

