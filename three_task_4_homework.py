n = int(input())
k = int(input())
permutation = [int(i) for i in input().split()]
buffer = []
for i in range(n):
    ma = [0,[0]*k]
    j = 0
    for element in input().split():
        if j > 0:
            ma[1][permutation[j - 1]-1] = int(element)
        else:
            ma[0] = element
        j+=1

    buffer.append(ma)

buffer.sort(key = lambda x: x[1], reverse = True)

for k in buffer:
    print(k[0])

    
        
        

        
            

