from collections import deque

s=input().split(" ")
n=int(s[0])
jump=int(s[1])
dq=deque([x for x in range(1,n+1)])
cnt=1
l=list()
while len(dq)!=0 :
    if cnt==jump : 
        l.append(dq.popleft())
        cnt=1
    else :
        dq.append(dq.popleft())
        cnt+=1
print('<'+str(l).strip("[] ")+'>')

# N, K = map(int, input().split())
# l = list(range(1, N+1))
# p = list()
# i = 0
# while l:
#     i = (i+K-1) % len(l)
#     p.append(str(l.pop(i)))

# print('<'+', '.join(p)+'>')
