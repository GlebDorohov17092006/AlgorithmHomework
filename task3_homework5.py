
n = int(input())
ma = [int(i) for i in input().split()]
ans = 0 #rколичество инверсий
def Merge(a,b):
    c, i, j, n1, n2 = [], 0, 0, len(a), len(b)
    global ans
    while(i < n1 or j < n2):
        if (j==n2 or (i < n1 and a[i]<=b[j])):
            c.append(a[i])
            i += 1
            ans += j
        else:
            c.append(b[j])
            j+=1
    return c

def MergeSort(Array):
    n = len(Array)
    if n==1:
        return Array
    else:
        a_sort = MergeSort(Array[0:n//2])
        b_sort = MergeSort(Array[n//2:])
        return Merge(a_sort,b_sort)
ma = MergeSort(ma)
print(ans)

