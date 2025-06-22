def brackets(s):
    stack = []
    for i in range(len(s)):
        ch = s[i]
        if ch == '(':
            if stack and stack[-1] == ')':
                if stack[-2] == '(' and s[i+1] == ')':
                    stack.append(ch)
                    continue
                else:
                    return True
            stack.append(ch)
        else:
            stack.append(ch)
    return False
t = int(input())
for _ in range(t):
    s = input()
    print("YES" if brackets(s) else "NO")