import sys
input = sys.stdin.readline

n,m=list(map(int,input().split()))
cost_list=[]

for i in range(m):
    n1,n2,cost=list(map(int,input().split()))
    cost_list.append((n1,n2,cost))
cost_list=sorted(cost_list,key=lambda x: x[2])

union_list=[_ for _ in range(n+1)]

def get_parent(node1):
    if union_list[node1]==node1:
        return node1
    else :
        parent=get_parent(union_list[node1])
        union_list[node1]=parent
        return parent

def make_union(parent,child):
    union_list[get_parent(child)]=get_parent(parent)

total_cost=0
line_num=0
for node1,node2,cost in cost_list:
    if get_parent(node1)!= get_parent(node2) :
        make_union(node1,node2)
        total_cost+=cost
        line_num+=1
    if line_num==n-1:
        break

print(total_cost)
