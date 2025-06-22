def isPalindrome(n):
    s = str(n)
    return s == s[::-1]

def divisors(n):
    ans = []
    for i in range(1,int(n**(1/2))+1):
        if n%i == 0:
            if isPalindrome(i):
                ans.append(i)
            if i*i != n and isPalindrome(n//i):
                ans.append(n//i)
    return ans

n = int(input())
ans = divisors(n)
print(','.join(map(str, sorted(ans))))