class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n=len(grid)
        m=len(grid[0])
        visit=[[False]*m for _ in range(n)]
        cnt=0 
        x=[0,1,0,-1]
        y=[1,0,-1,0]
        
        def bfs(grid,visit,i,j):
            stack=[(i,j)]
            while stack:
                nowy,nowx= stack.pop()
                for k in range(4):
                    newy,newx=nowy+y[k],nowx+x[k]
                    if newx<0 or newx>=m or newy<0 or newy>=n or visit[newy][newx]==True or grid[newy][newx]=='0':
                        continue
                    visit[newy][newx]=True
                    stack.append((newy,newx))
                
        
        for i in range(n):
            for j in range(m):
                if grid[i][j]=='1' and visit[i][j]==False:
                    visit[i][j]=True
                    bfs(grid,visit,i,j)
                    cnt+=1
        return cnt
       
            
            