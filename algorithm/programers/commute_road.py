def solution(m, n, puddles):
    map=[[0]*(n+1) for i in range(m+1)]
    map[0][1]=1
    for (i,j) in puddles:
        map[i][j]=-1
    for i in range(1,m+1):
        for j in range(1,n+1):
            if map[i][j]==-1:
                map[i][j]=0
            else :
                map[i][j]=(map[i-1][j]+map[i][j-1])%1000000007

    return map[m][n]