def walker(dirs):
    directions={'L':(0,-1),'R':(0,1),'U':(1,0),'D':(-1,0)}
    answer=0
    visit=[[False]*11 for i in range(11)]
    visit[5][5]=True
    
    updown_set=set()
    leftright_set=set()
    x,y=5,5
    for dir in dirs:
        #새로 이동할 좌표
        newx,newy=x+directions[dir][1],y+directions[dir][0]
        if newx<0 or newx>10 or newy<0 or newy>10: #벽에 부딪히면 그대로 둠
            newx,newx=x,y
            continue
        if dir=='L' or dir=='R': #좌우 이동
            leftright_set.add((y,min(x,newx),max(x,newx)))
        else : #상하 이동
            updown_set.add((x,min(y,newy),max(y,newy)))
            
        visit[newy][newx]=True
        x,y=newx,newy
    
    return len(leftright_set)+len(updown_set)

def solution(dirs):
    return walker(dirs)