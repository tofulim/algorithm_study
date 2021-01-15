a=[1,2,3]
b=["a","b","a"]
s={x : y for x,y in zip(a,b)}

l=s.items()
c=list(zip(s.keys(),s.values()))
print(c[0][1])