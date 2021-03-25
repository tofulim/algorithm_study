class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        x=[0,0,1,1,1,-1,-1,-1]
        y=[1,-1,-1,0,1,-1,0,1]
        n=len(board)
        m=len(board[0])
        def deadOralive(board,i,j):
            alive_cnt=0
            for k in range(8):
                newy=i+y[k]
                newx=j+x[k]
                if newy<0 or newy>=n or newx<0 or newx>=m:
                    continue
                if board[newy][newx]==1 or board[newy][newx]==-1:
                    alive_cnt+=1
                
            if board[i][j]==0 and alive_cnt==3 :
                return 3 #revibe
            elif board[i][j]==1 :
                return  1 if alive_cnt==3 or alive_cnt==2 else -1
        
        for i in range(n):
            for j in range(m):
                board[i][j]=deadOralive(board,i,j)
        for i in range(n):
            for j in range(m):
                board[i][j]=1 if board[i][j]==3 or board[i][j]==1 else 0
               
            