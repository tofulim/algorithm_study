cnt=0

def square(y,x,n,r,c):
    
    global cnt
    print("n",n,"cnt",cnt)
    if n==0:
        print("why",cnt)
        if y==r and x==c:
            print(cnt)
        elif r==y and x+1==c:
            print(cnt+1)
        elif r==y+1 and x==c:
            print(cnt+2)
        else :
            print(cnt+3)
    else :
        print("before",cnt)
        divider=2**(n-1)
        if r<divider and c<divider:
            square(y,x,n-1,r,c)
        elif r<divider and c>=divider:
            cnt+=2**n
            square(y,x+divider,n-1,r,c)
        elif r>=divider and c<divider:
            cnt+=2**n*2
            square(y+divider,x,n-1,r,c)
        elif r>=divider and c>divider:
            cnt+=2**n*3
            square(y+divider,x+divider,n-1,r,c)
        
         

N,r,c=list(map(int,input().split()))
square(0,0,N,r,c)