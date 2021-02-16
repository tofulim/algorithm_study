n=int(input())
hp=list(map(int,input().split()))
joy=list(map(int,input().split()))

visit=list()
max_joy=0

def now_or_never(now_hp,now_joy,idx):
    if now_hp<=0 : return
    if idx>=n :
        global max_joy
        max_joy=max(max_joy,now_joy)
        return

    now_or_never(now_hp-hp[idx],now_joy+joy[idx],idx+1)
    now_or_never(now_hp,now_joy,idx+1)
now_or_never(100,0,0)

print(max_joy)