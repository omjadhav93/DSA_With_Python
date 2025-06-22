def func(arr, n):
    if all(i ==0 for i in arr):
        return True
    x, y = [0]*n, [0]*n
    skip = True
    for i in range(1,n+1):
        x[i-1] = arr[i-1] - i
        if x[i-1] < 0:
            skip = False
            break
    if skip and func(x,n):
        return True
    skip = True
    for i in range(1,n+1):
        y[i-1] = arr[i-1] - (n-i+1)
        if y[i-1] < 0:
            skip = False
            break
    if skip and func(y,n):
        return True
    return False
    
        

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list( map(int, input().split()))
    print("YES" if func(arr,n) else "NO")