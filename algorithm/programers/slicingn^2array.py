#code1 - bfs

x=[0,1,1] # 우, 하 ,아래대각만 보면 되므로 3개
y=[1,0,1]
def bfs(arr,visit,n):
    queue=[(0,0,1)]
    visit[0][0]=True
    cnt_num=1 #초기 숫자1
    arr[0][0]=1
    while queue:
        i,j,cnt_num=queue.pop()
        cnt_num+=1 #다음 숫자로 증가시킴
        for k in range(3): #우, 하 ,아래대각 순회하며 조건 맞는지 검사
            newi=i+y[k]
            newj=j+x[k]
            if newi>=n or newj>=n or visit[newi][newj]:
                continue
            visit[newi][newj]=True
            queue.append((newi,newj,cnt_num)) #한칸 증가시킨다
            arr[newi][newj]=cnt_num #해당 증가한 값을 배열에 기록
    
    oned_arr=[]
    for a in arr: #1차원 배열로 결합
        oned_arr.extend(a)
    return oned_arr

def solution(n, left, right):
    arr=[[0 for i in range(n)] for j in range(n)]
    visit=[[False for i in range(n)] for j in range(n)]
    return bfs(arr,visit,n)[left:right+1] #1차원 배열을 인덱스 슬라이싱해 정답 도출

# code2 - use 2 for loop
#     answer=[]
#     for i in range(1,n+1):
#         for j in range(1,n+1):
#             answer.append(max(i,j))
        
#     return answer[left:right+1]

def solution(n, left, right): #위에서 수도코드를 쓰고 이를 한줄로 만든 풀이
    return [max(i,j) for j in range(1,n+1) for i in range(1,n+1)][left:right+1]

# code3(answer) - get partial array
def solution(n, left, right):
    #divide left & right to get row n col 
    return [max(int(idx//n)+1,(idx%n)+1) for idx in range(left,right+1)] 