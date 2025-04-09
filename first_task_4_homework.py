import random
def Partition(a,low,high,pivot):
    i,j= low,low
    while i <= high:
        if a[i]<pivot:
            a[j],a[i] = a[i],a[j]
            j+=1
        i+=1
    k,i = j,j
    while i <= high:
        if a[i]==pivot:
            a[k],a[i] = a[i],a[k]
            k+=1
        i+=1
    return j-1,k

def QuickSort(a,low,high):
    if low<high:
        pivot = random.randint(low,high)
        j,k = Partition(a,low,high,a[pivot])
        QuickSort(a,low,j)
        QuickSort(a,k,high)

class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        QuickSort(nums,0, len(nums)-1)
        return nums
print(Solution().sortArray([32,23,24,343,22,223222,342,2,23,34,22,22,34,8,6,54,43,2,2,24,6,6543,33,4,56,6]))