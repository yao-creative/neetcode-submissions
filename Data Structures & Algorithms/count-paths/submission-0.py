class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # down or right so it probably came from right or down.
        dp  = [[0 for _ in range(m)]  for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if i == 0 and j == 0:
                    # print(f"both 0")
                    dp[i][j] = 1
                    # print(f"dp: {dp}")
                    continue

                summand = 0
                if j > 0: # there's row above  continue
                    summand += dp[i][j-1] 
                if i > 0:
                    summand += dp[i-1][j]
                dp[i][j] = summand
        # print(f"dp: {dp}")
        return dp[-1][-1]
        