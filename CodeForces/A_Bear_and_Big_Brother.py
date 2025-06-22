limak, bob = map(int, input().split())
n = 0
while limak <= bob:
    n += 1
    limak *= 3
    bob *= 2
print(n)