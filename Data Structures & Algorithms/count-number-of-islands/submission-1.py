from typing import List

# def print_grid(grid):
#     for i, row in enumerate(grid):
#         print(' '.join(str(cell) for cell in row))
#         print()
   

class UnionFind:
    def __init__(self, grid):
        self.parent = [[(0,0) for _ in range(len(grid[0]))] for _ in range(len(grid))]
        self.grid = [[int(grid[i][j]) for j in range(len(grid[0]))] for i in range(len(grid))] #integerify it
        #initialize singleton equivalence classes 
        for i in range(len(grid)): #vertical
            for j in range(len(grid[0])): #horizontal
                self.parent[i][j] = (i,j)  # (vertical, horizontal)

        # print(f"self.grid:")
        # print_grid(self.grid)


    def find(self, x):
        while self.parent[x[0]][x[1]] != x: #(vertical, horizontal) search all the way to equivalence class roots.
            x = self.parent[x[0]][x[1]]
        return x

    def union(self, x, y):
        #combine the equivalence classes
        px, py = self.find(x), self.find(y)
        if px != py:
            self.parent[px[0]][px[1]] = py
        
    def get_unique_count(self) -> int:
        # unique count of parent over the grid.
        unique_map = set()
        # counter = 0
        # go through equivalence classes
        for i in range(len(self.parent)): #vertical 
            for j in range(len(self.parent[0])): #horizontal
                if self.grid[i][j] == 1:
                    island = self.find((i,j))
                    if island not in unique_map: #find if the island is registered before by equivalence class.
                        unique_map.add(island)
                   
                # else connected to something else already.
        # print("final parent:")
        # print_grid(self.parent)
        return len( unique_map)

    def scan(self, pos) -> List[int]: # up and #left 
        res = {"up": False, "left": False}
        if pos[0] - 1 >= 0 and self.grid[pos[0] - 1][pos[1]] == 1:  #vertical is land
            res["up"] = True
        if pos[1] - 1 >= 0 and self.grid[pos[0]][pos[1] - 1] == 1 :  #horizontal is land
            res["left"] = True
        # (should merge left, should merge up) 
        # print(f"scanning: {pos}, res: {res}")
        return res
        
                

# 0 1 0
# 1 1 0
# 0 0 0

# then if up and left but up and left are different groups, everyone on left needs to merge to up or merge left, actually it doesn't matter since they all are assumed to be stable,
# having one or another in same island as equivalence class rep doesn't matter

# 1 0 1 0
# 1 1 1 0
# 0 0 0 0
        

class Solution:

    def numIslands(self, grid: List[List[str]]) -> int:
        uf = UnionFind(grid)
        # the invariant for iterating through the grid is that previous cells Left to Right and Top to Bottom are already in their unique partitions based on their neighbors or fixed as root nodes
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # print(f"grid[{i}][{j}]: {grid[i][j]}")
                if grid[i][j] == "1": # check if landbridge then merge
                    res = uf.scan((i,j))
                    #merge up first prio then left
                    if res["up"]: 
                        # union up
                        # print("union up")
                        uf.union((i, j), (i - 1, j))
                    if res["left"]:
                        # print("union left")

                        uf.union((i, j), (i, j - 1))
                #oceans don't matter so can skip

        return uf.get_unique_count()

                # else nothing, one can add to the case of the 0 ocean.
                



                

        
                