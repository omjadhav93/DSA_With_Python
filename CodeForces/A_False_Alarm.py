t = int(input())
for _ in range(t):
    n, x = map(int, input().split())
    arr = list( map(int, input().split()))
    if x >= n:
        print("YES")
        continue
    first, last = -1, -1
    for i in range(n):
        if arr[i]:
            first = i
            break
    for i in range(n-1,-1,-1):
        if arr[i]:
            last = i
            break
    print("YES" if last-first+1 <= x else "NO")