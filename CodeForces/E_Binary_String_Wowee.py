import sys

# def countWays(s, n, k, curr):
    # Backtracking

t = int(sys.stdin.readline())
for _ in range(t):
    n, k = map(int, sys.stdin.readline().split())
    s = sys.stdin.readline()
    ans = 0
    for i in range(n):
        if s[i] == '0':
            curr = 0
            r = i
            while r < n:
                arr1 = [0]*n
                j = r
                new_str = s
                while j < n and curr < k:
                    arr = [0]*n
                    for x in range(j+1):
                        if (new_str[x] == '1'):
                            new_str = new_str[:x]+'0'+new_str[x+1:]
                        else:
                            new_str = new_str[:x]+'1'+new_str[x+1:]
                    arr[j] = 1
                    j = 0
                    curr += 1
                    while j < n and (arr[j] == 1 or new_str[j] == '1'):
                        j += 1
            if curr >= k:
                ans += 1
    sys.stdout.write(str(ans%998244353)+'\n')
                
                    