import sys

def slices(n, m, a, b, row, res = 1):
    if n == m == 1:
        return res
    if row and m > 1:
        cut3 = m-b
        cut4 = b-1
        new_m = m - max(cut3,cut4)
        res += 1
        return slices(n,new_m,(n//2)+1,(new_m//2)+1,False,res)
    else: 
        cut1 = n-a
        cut2 = a-1
        new_n = n-max(cut1,cut2)
        res += 1
        return slices(new_n,m,(new_n//2)+1,(m//2)+1,True,res)

t = int(sys.stdin.readline())
for _ in range(t):
    n, m, a, b = map(int, sys.stdin.readline().split())
    if n == m == 1:
        sys.stdout.write(str(0)+"\n")
        continue
    cut1 = n-a
    cut2 = a-1
    cut3 = m-b
    cut4 = b-1
    mx = max(cut1,cut2,cut3,cut4)
    res = 0
    if cut1 == mx or cut2 == mx:
        new_n = n-mx
        res = slices(new_n,m,(new_n//2)+1,(m//2)+1,True)
    else:
        new_m = m-mx
        res = slices(n,new_m,(n//2)+1,(new_m//2)+1,False)
    sys.stdout.write(str(res)+"\n")
        