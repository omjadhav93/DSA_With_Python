t = int(input())
for _ in range(t):
    n = int(input())
    arr = sorted(map(int, input().split()))
    ans = float('inf')
    if arr[0]&1:
        for i in range(n-1,-1,-1):
            if arr[i]&1:
                ans = min(ans, n-i-1)
    else:
        for i in range(n-1,-1,-1):
            if arr[i]&1 == 0:
                ans = min(ans, n-i-1)
    if arr[n-1]&1:
        for i in range(0,n,):
            if arr[i]&1:
                ans = min(ans, i)
    else:
        for i in range(0,n,):
            if arr[i]&1 == 0:
                ans = min(ans, i)
    print(ans)