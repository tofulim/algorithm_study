class Node:
    del_list=[]
    def __init__(self,node):
        self.index=node
        self.right=None
        self.left=None
    def get_num(self):
        return self.index
    
    def up(self,cnt):
        now_node=self
        while cnt!=0:
            if now_node.left==None:
                break
            now_node=now_node.left
            cnt-=1
        return now_node
    
    def down(self,cnt):
        now_node=self
        while cnt!=0:
            if now_node.right==None:
                break
            now_node=now_node.right
            cnt-=1
        return now_node
    
    def delete(self):
        now_node=self
        num=now_node.get_num()
        self.del_list.append(now_node)
        if now_node.right==None:
            now_node=now_node.left
            now_node.right=None
        elif now_node.left==None:
            now_node=now_node.right
            now_node.left=None
        else:
            now_node.left.right=now_node.right
            now_node.right.left=now_node.left
            now_node=now_node.right
        return now_node, num
    
    def drawback(self):
        drawback_node=self.del_list.pop()
        if drawback_node.left!=None:
            drawback_node.left.right=drawback_node
        if drawback_node.right!=None:
            drawback_node.right.left=drawback_node
            
        return drawback_node.get_num()
            
        
def solution(n, k, cmd):
    answer=["O"]*n
    curser=Node(0)
    tmp_node=curser
    #연결리스트 노드 연결
    for num in range(1,n):
        new_node=Node(num)
        tmp_node.right=new_node
        new_node.left=tmp_node
        tmp_node=new_node
        
    # print("초기 커서값 이동 전",curser.get_num())
    #초기 커서값 이동
    for cur_cnt in range(k):
        curser=curser.right
    # print("초기 커서값 이동 후",curser.get_num())
    #명령어 실행
    for command in cmd:
        if len(command)>=3:
            command=command.split()
            number=int(command[1])
            if command[0]=="D":
                curser=curser.down(number)
            elif command[0]=="U":
                curser=curser.up(number)
                
        elif command[0]=="C":
            curser,num=curser.delete()
            answer[num]="X"
        else:
            num=curser.drawback()
            answer[num]="O"
        # print(f"{command}수행후 curser의 위치는 {curser.get_num()}")
            
        
    return ''.join(answer)