nums1 = [int(i) for i in input().split()]
nums2 = [int(i) for i in input().split()]

def help_func(n: int,m: int,mid1: int,mid2: int) -> tuple[float]:
    if (mid1 < 1):
        ma_1 = float('-inf')
    if (mid1 >= 1):
        ma_1 = nums1[mid1-1]
    if (mid1 >= m):
        mi_1 = float('inf')
    if (mid1 < m):
        mi_1 = nums1[mid1]
    if (mid2 < 1):
        ma_2 = float('-inf')
    if (mid2 >= 1):
        ma_2 = nums2[mid2-1]
    if (mid2 >= n):
        mi_2 = float('inf')
    if (mid2 < n):
        mi_2 = nums2[mid2]
    return (ma_1,ma_2,mi_1,mi_2)

def median(nums1: list[int], nums2: list[int]) -> float:
    left ,right, m, n = 0, len(nums1), len(nums1), len(nums2)
    while left<=right:
        mid1, mid2 = (left + right)//2, (m + n + 1)//2 - (left + right)//2

        ma_1, ma_2, mi_1, mi_2 = help_func(n, m, mid1, mid2)

        if (ma_1 <= mi_2) and (ma_2 <= mi_1):
            if (m+n)%2==0:
                return (max(ma_1,  ma_2) + min(mi_1,mi_2))/2
            return max(ma_1, ma_2 )
        elif (ma_1>mi_2):
            right = mid1 - 1
        else:
            left = mid1 + 1

print(median(nums1, nums2))
        
        