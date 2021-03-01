import math
class Solution:
    def numSquares(self, n: int) -> int:
        dp=[n for _ in range(n+1)]
        dp[1]=1
        for i in range(2,n+1):
            if math.sqrt(i).is_integer():
                dp[i]=1
            else:
                sqrt_val=int(math.sqrt(i))
                for j in range(1,sqrt_val+1):
                    dp[i]=min(dp[i],dp[i-j**2]+dp[j**2])
        return dp[n]

#정답
import math
class Solution:
    def numSquares(self, n: int) -> int:
        if n<3 : return n
        
        dp=[n for _ in range(n+1)]
        square=[k**2 for k in range(0, int(math.sqrt(n))+1)]
        dp[0]=0
        for i in range(1,n+1):
            for j in square:
                if i<j : break;
                dp[i]=min(dp[i],dp[i-j]+1)
        
        return dp[-1]
        