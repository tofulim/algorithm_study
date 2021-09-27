x=[0,1,0,-1]
y=[-1,0,1,0]

def bfs_walker(maps, visit,n,m):
    answer=100000
    visit[n-1][m-1]=True
    stack=[(n-1,m-1,1)]
    while stack:
        i,j,cnt=stack.pop(0)
        if i==0 and j==0:
            return cnt
        for k in range(4):
            newx=j+x[k]
            newy=i+y[k]
            if newx<0 or newx>=m or newy<0 or newy>=n or maps[newy][newx]==0 or visit[newy][newx]:
                continue
            stack.append((newy,newx,cnt+1))
            visit[newy][newx]=True
            
    return -1

def solution(maps):
    n,m=len(maps),len(maps[0])
    visit=[[False]*m for i in range(n)]
    visit[n-1][m-1]=True
    return bfs_walker(maps, visit,n,m)