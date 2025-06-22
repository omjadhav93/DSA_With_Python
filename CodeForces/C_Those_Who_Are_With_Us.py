for _ in range(int(input())):
    n, m = map(int, input().split())
    arr = []
    for i in range(n):
        arr.append(list(map(int, input().split())))
    row, col = [0], [0]
    mx = arr[0][0]
    for i in range(n):
        for j in range(m):
            if arr[i][j] > mx:
                mx = arr[i][j]
                row, col = [i], [j]
            elif arr[i][j] == mx:
                row.append(i)
                col.append(j)
    mx -= 1
    r, c = row[0], None
    for i in range(len(row)):
        if r != row[i]:
            if not c: c = col[i]
            elif c != col[i]:
                mx += 1
                break
    print(mx)