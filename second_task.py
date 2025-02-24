n, k = map(int, input().split())
ma = [int(i) for i in input()]
ind = [0]
for i in range(n-1):
    if ma[i]:
        ind.append(i+1)
ind.append(n)
def check(ind: list[int],k: int, mid: int) -> bool:
    j = 0
    i = 1
    ans = 1
    while i < len(ind):
        delta = ind[i] - ind[j]
        if delta>mid:
            if (i - j)==1:
                return False
            else:
                ans+=1
                j = i - 1
        elif delta==mid:
            ans+=1
            j = i
            i+=1
        else:
            if i==len(ind):
                ans+=1
            i += 1
    return ans<=k
                         
            
def bin_search(n: int, k: int, ma: list[int], ind: list[int]) -> int:
    left = 0
    right = n
    while (right-left)>1:
        mid = (right+left)//2
        if check(ind, k, mid):
            right = mid
        else:
            left = mid
    if check(ind, k, left):
        return left
    return right

print(bin_search(n,k,ma, ind))