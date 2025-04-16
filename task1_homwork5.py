n = int(input())
life = []
for i in range(n):
    day1, month1, year1, day2, month2, year2 = map(int, input().split())
    if [year2, month2, day2] >= [year1 + 18, month1, day1]:
        life.append([[year1 + 18, month1, day1], 1])
        life.append([min([year1+80, month1, day1], [year2, month2, day2]),-1])
life.sort(key=lambda x: (x[0], x[1]))
k = 0
max_sovrem = 0
for elem in life:
    k += elem[1]
    max_sovrem = max(k, max_sovrem)
print(max_sovrem)


    

        

    

    