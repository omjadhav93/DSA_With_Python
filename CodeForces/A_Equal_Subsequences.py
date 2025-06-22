for _ in range(int(input())):
    n, k = map(int, input().split())
    s = ['1']*k
    if len(s) < n:
        s.append('0')
    while len(s) < n:
        s.insert(1,'0')
    print(''.join(s))