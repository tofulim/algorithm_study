n=int(input())
arr=[]
for i in range(0,n):
    tmp=int(input())
    arr.append(tmp)
arr=sorted(arr)
for j in range(0,n):
    print(arr[j])