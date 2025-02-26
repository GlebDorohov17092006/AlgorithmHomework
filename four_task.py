n, m = map(int, input().split())
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]

def bin_search(n: int, m: int, a: list[int], b: list[int]) -> list[int]:
    answer = []
    for x in b:
        left = 0
        right = n-1
        while (right - left)>1:
            mid = (right + left)//2
            if a[mid] < x:
                left = mid
            else:
                right = mid
        if a[left]>=x:
            answer.append(left)
        else:
            answer.append(right)
    return answer

print(*bin_search(n,m,a,b))
        
