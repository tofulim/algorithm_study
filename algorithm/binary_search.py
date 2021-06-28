import bisect
#이진탐색 구현 & bisect로 구현
a=[1,3,7,3,3,5,2,9]

# def bin_search(arr,key):
#     arr.sort()
#     print(arr)
    
#     start,end=0,len(a)-1
#     mid=0
#     while start<=end:
#         mid=(start+end)//2
#         if key<=arr[mid]:
#             end=mid-1
#         elif arr[mid]<key:
#             start=mid+1
#     return start

# print(bin_search(a,3))
a.sort()
print(a)
index=bisect.bisect(a,3,lo=0,hi=len(a))
print(f'bisect result : {index}')

index=bisect.bisect_left(a,3,lo=0,hi=len(a))
print(f'bisect_left result : {index}')

index=bisect.bisect_right(a,3,lo=0,hi=len(a))
print(f'bisect_right result : {index}')

bisect.insort(a,4,lo=0,hi=len(a))
print(f'bisect_insort 4 result : {a}')
