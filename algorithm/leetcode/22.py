class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        answer=set()
        string=''
        cycle(n,n,string,answer)
        return list(answer)

def cycle(open_c,close_c,string,answer):
    if open_c==0 and close_c==0 : 
        answer.add(string)
        return
    if open_c==0 and close_c !=0 :
        answer.add(string+')'*close_c)
        return
    if open_c==close_c : 
        cycle(open_c-1,close_c,string+'(',answer)
    else :
        cycle(open_c-1,close_c,string+'(',answer)
        cycle(open_c,close_c-1,string+')',answer)
        
    
        
# import itertools
# class Solution:
#     def generateParenthesis(self, n: int) -> List[str]:
#         permutations='()'*n
#         permutations=list(set(itertools.permutations(permutations)))
#         return [''.join(l) for l in permutations if check(l)]

# def check(l):
#     if l[0]==')' : return False
#     stack = [l[0]]
#     for i in range(1,len(l)):
#         if l[i]=='(' : stack.append(l[i])
#         elif l[i]==')' :
#             if len(stack)>0 and stack[-1]=='(' :
#                 stack.pop()
#             else : return False
#     return True if len(stack)==0 else False