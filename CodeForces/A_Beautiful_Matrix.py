arr = []
i, j = 0, 0
for k in range(5):
    arr.append(list(map(int, input().split())))
    if 1 in arr[k]:
        i = k
        j = arr[i].index(1)
print(abs(i-2)+abs(j-2))