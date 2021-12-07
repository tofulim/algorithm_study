def commonChild(s1, s2):
    # Write your code here
    str_len=len(s1)
    dp=[[0]*(str_len+1) for _ in range(str_len+1)] # n+1*n+1 dp 배열 생성
    for i in range(1,str_len+1):
        for j in range(1,str_len+1):
            if s1[j-1]==s2[i-1]: #대각선+1, 상, 좌 중 큰 값
                dp[i][j]=max(dp[i-1][j-1]+1,max(dp[i][j-1],dp[i-1][j]))
            else: #다르다면 상, 좌 중 큰 값
                dp[i][j]=max(dp[i][j-1],dp[i-1][j])
                
    return dp[str_len][str_len]