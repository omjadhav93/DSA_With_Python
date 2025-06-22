def countOnes(n):
    cnt = 0
    while n:
        if n&1:
            cnt += 1
        n >>= 1
    return cnt

for _ in range(int(input())):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    beauty, evens = 0, 0
    for num in arr:
        beauty += countOnes(num)
        if num&1 == 0:
            evens += 1
    if evens >= k:
        beauty += k
    else:
        beauty += evens
    print(beauty)