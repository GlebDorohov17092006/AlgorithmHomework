import matplotlib.pyplot as plt

n = int(input())
ma = []
for i in range(n):
    x, y = map(int, input().split())
    ma.append([x,y])
ma.sort()
print("Ответ:")
for j in range(n):
    print(*ma[j])

'''Дополнительная визуализация'''

plt.plot([ma[i][0] for i in range(n)], [ma[i][1] for i in range(n)], marker='o', linestyle='-', color='b')
plt.show()