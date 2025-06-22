t = int(input())
for _ in range(t):
    s = input()
    n1, op, n2 = '', '', ''
    first = True
    for i in range(len(s)):
        if s[i] in ('+','-','*'):
            op = s[i]
            first = False
        elif first:
            n1 += s[i]
        else:
            n2 += s[i]
    num1 = int(n1)
    num2 = int(n2)
    n2 = op + n2
    l1, l2 = len(n1), len(n2)
    if op == '+':
        ans = str(num1+num2)
        l3 = len(ans)
        mx = max(l1, l2, l3)
        while mx > l1:
            n1 = ' '+n1
            l1 += 1
        while mx > l2:
            n2 = ' '+n2
            l2 += 1
        while mx > l3:
            ans = ' '+ans
            l3 += 1
        print(n1)
        print(n2)
        print(''.join(['-']*mx))
        print(ans)
    elif op == '-':
        ans = str(num1-num2)
        l3 = len(ans)
        mx = max(l1, l2, l3)
        while mx > l1:
            n1 = ' '+n1
            l1 += 1
        while mx > l2:
            n2 = ' '+n2
            l2 += 1
        while mx > l3:
            ans = ' '+ans
            l3 += 1
        print(n1)
        print(n2)
        print(''.join(['-']*mx))
        print(ans)
    elif op == '*':
        ans = []
        while num2 > 0:
            ans.append(num1*(num2%10))
            num2 //= 10
        product = str(sum(ans[i]*(10**i) for i in range(len(ans))))
        ans = [str(num) for num in ans]
        l3 = len(product)
        nMax = max(l1,l2)
        mx = max(l1, l2, l3)
        while mx > l1:
            n1 = ' '+n1
            l1 += 1
        while mx > l2:
            n2 = ' '+n2
            l2 += 1
        while mx > l3:
            product = ' '+product
            l3 += 1
        for i in range(len(ans)):
            curr = len(ans[i])
            ans[i] = ''.join([' ']*(mx-curr-i)) + ans[i] + ''.join([' ']*i)
        print(n1)
        print(n2)
        if len(ans) > 1:
            print(''.join([' ']*(mx-nMax)) + ''.join(['-']*nMax))
            for num in ans:
                print(num)
        print(''.join(['-']*mx))
        print(product)
    print()
        