n,m=list(map(int,input().split()))
map1=[[1 if x=='X' else 0 for x in input()] for _ in range(n)]
map2=[[1 for _ in range(m)] for _ in range(n)]
x=[0,1,0,-1]
y=[1,0,-1,0]
def solo(i,j):
    cnt=0
    for k in range(4):
        newx=j+x[k]
        newy=i+y[k]
        if newy<0 or newx<0 or newy>=n or newx>=m or map1[newy][newx]==0:
            cnt+=1
    return True if cnt>=3 else False

minx,miny=m-1,n-1
maxx,maxy=0,0
for i in range(n):
    for j in range(m):
        if map1[i][j]==1 :
            if solo(i,j) :
                map2[i][j]=0
            else:
                minx=min(minx,j)
                miny=min(miny,i)
                maxx=max(maxx,j)
                maxy=max(maxy,i)

for print_y in range(miny,maxy+1):
    print(''.join(['X' if map1[print_y][print_x]==1 and map2[print_y][print_x]==1 else '.' for print_x in range(minx,maxx+1)]))