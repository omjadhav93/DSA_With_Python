n, k = map(int, input().split())
arr = list(map(int, input().split()))
i = 0
if arr[k-1] != 0:
    while i < n and arr[i] >= arr[k-1]:
        i += 1
else:
    while i < n and arr[i] > arr[k-1]:
        i += 1
print(i)