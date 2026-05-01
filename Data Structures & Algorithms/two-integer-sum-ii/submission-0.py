from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers)- 1

        while i < j < (len(numbers)):
            # print(f"i: {i}, j:  {j}, numbers[{i}]: {numbers[i]}, numbers[{j}]: {numbers[j]}")
            if numbers[i] + numbers[j] == target:
                return [i + 1, j + 1] #one indexed
            if numbers[i] + numbers[j] < target:
                i+=1
            else:
                j-=1
        return [i + 1, j + 1] #one indexed
