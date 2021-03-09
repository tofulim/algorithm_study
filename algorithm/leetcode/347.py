from collections import Counter
import heapq
a=[3,0,1,0]
cnt=Counter(a)
print([k for k,v in cnt.most_common(n=2)])
print(heapq.nlargest(1, cnt.keys(), key=cnt.get) )