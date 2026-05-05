class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0 :
            return 1
        dp = [0] * (n + 1)
        for i in range(n + 1): # 0 to n-1
            # print(f"i: {i}")
            if i == 0:
                dp[i] = 1
            elif i == 1:
                dp[i] = 1
            else:
                dp[i] = dp[i-1] + dp[i-2] 
        # print(f"dp: {dp}")
        return dp[n]
                