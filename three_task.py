n = int(input())
ma = [int(i) for i in input().split()]
def two_elements(n: int, ma: list[int]) -> int:
    i, j = n-1,n-1
    while True:
        i = ma[i]
        j = ma[ma[j]]
        if i==j:
            break

    j = n - 1
    while True:
        i = ma[i]
        j = ma[j]
        if i==j:
            return i
        
print(two_elements(n, ma))
            