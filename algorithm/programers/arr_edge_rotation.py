def rotation(num_map,query):
    i1,j1,i2,j2=query
    i1,j1,i2,j2=i1-1,j1-1,i2-1,j2-1
    ori_arr=[]
    min_num=0
    for j in range(j1,j2):
        ori_arr.append(num_map[i1][j])
    
    for i in range(i1,i2):
        ori_arr.append(num_map[i][j2])
    
    for j in range(j2,j1,-1):
        ori_arr.append(num_map[i2][j])
        
    for i in range(i2,i1,-1):
        ori_arr.append(num_map[i][j1])
    #최소값 찾기
    min_num=min(ori_arr)
    #배열 회전
    ori_arr=[ori_arr[-1]]+ori_arr[:-1]
    #기존 배열을 회전된 배열로 변경
    for j in range(j1,j2):
        num_map[i1][j]=ori_arr.pop(0)
    
    for i in range(i1,i2):
        num_map[i][j2]=ori_arr.pop(0)
    
    for j in range(j2,j1,-1):
        num_map[i2][j]=ori_arr.pop(0)
        
    for i in range(i2,i1,-1):
        num_map[i][j1]=ori_arr.pop(0)
    
    return min_num

def solution(rows, columns, queries):
    answer = []
    num_map=[[0]*columns for _ in range(rows)]
    cnt=1
    for i in range(rows):
        for j in range(columns):
            num_map[i][j]=cnt
            cnt+=1
            
    for query in queries:
        answer.append(rotation(num_map,query))
        
    return answer