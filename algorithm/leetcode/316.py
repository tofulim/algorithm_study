from collections import Counter
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        str_dict=Counter(s)
        stack=[]    
        for char in s:
            if str_dict[char]>0 and char not in stack:
                str_dict[char]-=1
                if stack:
                    while stack and str_dict[stack[-1]] and char<stack[-1]:
                        stack.pop()
                stack.append(char)
            else : 
                str_dict[char]-=1
                
        return ''.join(stack)