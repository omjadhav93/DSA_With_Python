s = input()
a, b, n = 1, 0, 0
notE = True
for i in range(len(s)):
    ch = s[i]
    if ch == 'e':
        notE = False
        a = float(s[:i])
        b = int(s[i+1:])
if notE:
    n = float(s)
else:
    n = a*(10**b)
print(int(n) if n - round(n) == 0 else n)