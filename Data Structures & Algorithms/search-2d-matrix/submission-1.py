from typing import List

class Solution:

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # flat = []
        # for l in matrix: #flattening is n + log(mn)
        #     flat += l

        #binary search the range by using the first index then binary search the exact value
        left = 0
        right = len(matrix) -1 
        mid = -1
        while left <= right:
            mid = left + (right - left)//2
            # print(f"left: {left}, right: {right}, mid: {mid}")
            if target > matrix[mid][0]:
                #go mid and above (right)
                left = mid + 1
            elif target < matrix[mid][0]: 
                right = mid - 1 #below mid
            else: #equal then just return 
                return True
        # print(f"mid: {mid}")
        left_inner = 0
        right_inner = len(matrix[0]) -1
        while left_inner <= right_inner:
            mid_inner = left_inner + (right_inner - left_inner)//2
            if target > matrix[right][mid_inner]:
                #go mid and above (right)
                left_inner = mid_inner + 1
            elif target < matrix[right][mid_inner]: 
                right_inner = mid_inner - 1 #below mid
            else: #equal then just return 
                return True
        else:
            return False


            

            