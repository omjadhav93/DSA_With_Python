n = int(input())
x = 0
for _ in range(n):
    s = input()
    if s.find('++') != -1:
        x += 1
    if s.find('--') != -1:
        x -= 1
print(x)