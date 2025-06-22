for _ in range(int(input())):
    n, s = map(int, input().split())
    arr = list(map(int, input().split()))
    print(min(abs(s-arr[0]),abs(s-arr[n-1])) + (arr[n-1] - arr[0]))