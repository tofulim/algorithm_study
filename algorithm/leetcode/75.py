class Solution:
    
    def sortColors(self, nums: List[int]) -> None:
        return bubbleSort(nums)
    
def swap(l,a,b):
        tmp=l[a]
        l[a]=l[b]
        l[b]=tmp
    
def bubbleSort(l):
    for i in range(len(l)-1,0,-1):
        for j in range(0,i):
            if l[j]>l[j+1]: swap(l,j,j+1)
    return l