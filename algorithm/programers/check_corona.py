x=[0,1,0,-1]
y=[1,0,-1,0]

def bfs(i,j,place,visit):
    queue=[(i,j)]
    visit[i][j]=1
    while queue:
        top_y,top_x=queue.pop(0)
        for k in range(4):
            newx=top_x+x[k]
            newy=top_y+y[k]
            if newx<0 or newx>4 or newy<0 or newy>4 or visit[newy][newx]==1 or (abs(i-newy)+abs(j-newx))>2 or place[newy][newx]=='X':
                continue
            if place[newy][newx]=='P':
                return 0
            visit[newy][newx]=1
            queue.append((newy,newx))
    
    return 1

def check_corona(place):
    for i in range(5):
        for j in range(5):
            if place[i][j]=='P':
                visit=[[0]*5 for i in range(5)]
                if bfs(i,j,place,visit)==0:
                    return 0
    return 1
    
def solution(places):
    answer = []
    for place in places:
        answer.append(check_corona(place))
    return answer