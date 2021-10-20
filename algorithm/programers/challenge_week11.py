x=[0,1,0,-1,1,1,-1,-1] #상하좌우 대각
y=[1,0,-1,0,-1,1,1,-1]

def draw(rectangle): #모든 직사각형들의 합집합 배열을 구한다
    location_map=[[False]*101 for _ in range(101)]
    for rec in rectangle:
        x1,y1,x2,y2=rec
        for yy in range(y1,y2+1):
            for xx in range(x1,x2+1):
                location_map[yy][xx]=True
    return location_map

def is_inner_point(now_y,now_x,location_map): # 내부의 점인지 확인한다
    cnt=0
    for i in range(8):
        new_y=now_y+y[i]
        new_x=now_x+x[i]
        if new_y<0 or new_y>100 or new_x<0 or new_x>100 or not location_map[new_y][new_x]:
            continue
        else :
            cnt+=1
    return True if cnt==8 else False #모두 꽉차있다면 내부의 점, 아니면 테두리

def find_outline(rec_n,now_x,now_y,itemX,itemY,location_map): #BFS
    answer = float('inf')
    queue=[(now_y,now_x,0)]
    visit=[[False]*101 for _ in range(101)]
    visit[now_y][now_x]=True
    while queue:
        # print(queue)
        now_y,now_x,cost=queue.pop(0)
        if (now_y,now_x)==(itemY,itemX): #도착
            return cost
        for i in range(4):
            new_y=now_y+y[i]
            new_x=now_x+x[i]
            if new_x<0 or new_x>100 or new_y<0 or new_y>100 or visit[new_y][new_x] or not location_map[new_y][new_x] or is_inner_point(new_y,new_x,location_map) :
                continue
                
            queue.append((new_y,new_x,cost+1))
            visit[new_y][new_x]=True
                

def solution(rectangle, characterX, characterY, itemX, itemY):
    rec_n=len(rectangle)
    rectangle=list(map(lambda k: list(map(lambda k2:k2*2,k)), rectangle))
    #get rec_location_map
    location_map=draw(rectangle)
    return find_outline(rec_n,characterX*2,characterY*2,itemX*2,itemY*2,location_map)/2