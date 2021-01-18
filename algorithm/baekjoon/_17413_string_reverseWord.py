s=input()
l=len(s)
flag=False

new_s=""
rev_s=""
for i in range(0,l):
    if s[i]=='<' : 
        flag=True
        new_s+=rev_s[::-1]
        rev_s=""
        new_s+=s[i]
    elif s[i]=='>':
        new_s+=s[i]
        flag=False
    elif flag :
        new_s+=s[i]
    elif s[i]==' ':
        new_s+=rev_s[::-1]
        rev_s=""
        new_s+=s[i]
    else :
        rev_s+=s[i]
new_s+=rev_s[::-1]
print(new_s)