import sys

def checkTruth(arr, n):
    if arr.count(1) == n:
        return False
    for i in range(n):
        if i == 0:
            if arr[i] == 0 and arr[i+1] == 0:
                return False
        elif i == n-1:
            if arr[i] == 0 and arr[i-1] == 0:
                return False
        else:
            if arr[i] == 0 and (arr[i+1] == 0 or arr[i-1] == 0):
                return False
    return True
    

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))
    if checkTruth(arr,n):
        sys.stdout.write("NO\n")
    else:
        sys.stdout.write("YES\n")
    sys.stdout.flush()