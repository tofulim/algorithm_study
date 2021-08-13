def up(linked_dict,k,cnt):
    while cnt!=0:
        if linked_dict[k][0]==None:
            break
        k=linked_dict[k][0]
        cnt-=1
    return k

def down(linked_dict,k,cnt):
    while cnt!=0:
        if linked_dict[k][1]==None:
            break
        k=linked_dict[k][1]
        cnt-=1
    return k

def delete(linked_dict,delete_list,k):
    delete_list.append((k,linked_dict[k]))
    
    left,right=linked_dict[k]
    
    del linked_dict[k]
    if right==None:
        k=left
        linked_dict[left][1]=None
    elif left==None:
        k=right
        linked_dict[right][0]=None
    else:
        k=right
        linked_dict[left][1]=right
        linked_dict[right][0]=left
        
    return k

def drawback(linked_dict,delete_list):
    drawback_num,lr=delete_list.pop()
    left,right=lr
    if left!=None:
        linked_dict[left][1]=drawback_num
    if right!=None:
        linked_dict[right][0]=drawback_num
    linked_dict[drawback_num]=[left,right]
    
    return drawback_num
    
def solution(n, k, cmd):
    answer=["O"]*n
    linked_dict={i:[i-1,i+1] for i in range(n)}
    linked_dict[0]=[None,1]
    linked_dict[n-1]=[n-2,None]
    
    delete_list=[]
    #명령어 실행
    for command in cmd:
#         print(command)
        if len(command)>=3:
            command=command.split()
            number=int(command[1])
            if command[0]=="D":
                k=down(linked_dict,k,number)
            elif command[0]=="U":
                k=up(linked_dict,k,number)
        elif command[0]=="C":
            answer[k]="X"
            k=delete(linked_dict,delete_list,k)
            
            # print("del",''.join(answer))
        else:
            num=drawback(linked_dict,delete_list)
            answer[num]="O"
            # print("rec",''.join(answer))
            
    return ''.join(answer)