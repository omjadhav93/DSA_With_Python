def primeSeive(n):
    arr = [True]*(n+1)
    arr[0], arr[1] = False, False
    for i in range(2,int(n**(1/2))+1):
        if arr[i]:
            for j in range(i*i,n+1,i):
                arr[j] = False
    return arr

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    seive = primeSeive(m)
    for i in range(n, m+1):
        if seive[i]:
            print(i)
    print()