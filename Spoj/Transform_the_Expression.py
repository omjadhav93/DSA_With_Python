def postfix(exp: str):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3, '(': 0}
    stack = []
    res = ''
    for ch in exp:
        if ch == '(':
            stack.append(ch)
        elif ch.isalpha():
            res += ch
        elif ch == ')':
            while stack[-1] != '(':
                res += stack.pop()
            stack.pop()
        else:
            while stack and precedence.get(ch) <= precedence.get(stack[-1]):
                res += stack.pop()
            stack.append(ch)
    return res

t = int(input())
for _ in range(t):
    exp = input().strip()
    print(postfix(exp))