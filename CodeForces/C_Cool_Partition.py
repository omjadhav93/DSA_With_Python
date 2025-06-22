def backtrack(arr,dp, s = set(), i = 0, cnt = 0):
    if i == len(arr):
        return 0
    if dp[i] > 0:
        return dp[i]
    for j in range(i,n):
        if arr[j] in s:
            s.remove(arr[j])
        if len(s) == 0:
            s.update(arr[i:j+1])
            dp[i] = max(dp[i], 1 + backtrack(arr,dp,s,j+1,cnt+1))
            s.clear()
    return dp[i]
        
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    dp = [0]*n
    ans = backtrack(arr, dp)
    print(ans)