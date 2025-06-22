n, m, a = list(map(int, input().split()))
l = (n//a) if n%a == 0 else ((n//a)+1)
b = (m//a) if m%a == 0 else ((m//a)+1)
print(l*b)