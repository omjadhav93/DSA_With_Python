import sys

def isNine(num):
    return all(d == 9 for d in num)

def nextPalindrome(num, n):
    mid = n // 2
    i = mid - 1
    j = mid + 1 if n&1 else mid

    while i >= 0 and num[i] == num[j]:
        i -= 1
        j += 1
    
    check = (i < 0 or num[j] < num[i])
    
    while i >= 0:
        num[i] = num[j]
        j += 1
        i -= 1
    
    if check:
        carry = 1
        i = mid - 1
        if n&1:
            num[mid] += carry
            carry = num[mid] // 10
            num[mid] %= 10
            j = mid + 1
        else:
            j = mid
        
        while i >= 0 and carry >= 0:
            num[i] += carry
            carry = num[i] // 10
            num[i] %= 10
            num[j] = num[i]
            j += 1
            i -= 1

for _ in range(int(input())):
    n = int(input())
    rev = []
    while n > 0:
        rev.append(n%10)
        n //= 10
    digits = len(rev)
    ans = 0
    if isNine(rev):
        ans = 10**(digits) + 1
    else:
        nextPalindrome(rev, digits)
        ans = ''.join(str(num) for num in rev)
    
    print(ans)