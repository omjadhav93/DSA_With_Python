brackets = list(input())
m = int(input())
for _ in range(m):
    l, r = map(int, input().split())
    e = l
    l -= 1
    hit = []
    while l < r and e < r:
        if brackets[l] == '(' and brackets[e] == ')':
            hit += [l, e]
            while l in hit:
                l += 1
            while e in hit:
                e += 1
        while l < r and brackets[l] == ')':
            while l in hit:
                l += 1
        while e < r and brackets[e] == '(':
            while e in hit:
                e += 1
        if e <= l:
            e = l+1
    print(len(hit))