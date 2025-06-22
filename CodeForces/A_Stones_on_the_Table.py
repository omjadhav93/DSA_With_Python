n = int(input())
s = input()
ls = None
count = 0
for ch in s:
    if ch == ls:
        count += 1
    else:
        ls = ch
print(count)