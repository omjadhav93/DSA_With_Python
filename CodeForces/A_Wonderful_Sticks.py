n = int(input())
for i in range(n):
    k = int(input())
    s = input()
    arr = []
    i, j = 1, k
    for x in range(len(s)-1, -1, -1):
        if s[x] == '<':
            arr.insert(0, i)
            i += 1
        else:
            arr.insert(0, j)
            j -= 1
    arr.insert(0, i)
    print(*arr)