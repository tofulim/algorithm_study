s=input()
s=s.lower()
alpha=[0 for _ in range(26)]
for i in range(len(s)):
    c=s[i]
    alpha[ord(c)-97]+=1

max_alpha=max(alpha)
max_idx=-1
flag=False

for c in range(26):
    if alpha[c]==max_alpha:
        if flag:
            flag=False
            break
        else :
            flag=True
            max_idx=c 

print("?" if flag==False else chr(max_idx+97).upper())


# s,a=input().lower(),[]
# for i in range(97,123):
#  a.append(s.count(chr(i)))
# print('?'if a.count(max(a))>1 else chr(a.index(max(a))+97).upper())
