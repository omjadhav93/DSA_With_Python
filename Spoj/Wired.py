for _ in range(int(input())):
    arr = list(map(int, input().split()))
    brr = list(map(int, input().split()))
    match = [0]*4
    for i in range(4):
        match[brr[i]-1] = i
    print(*[match[arr[i]-1]+1 for i in range(4)])