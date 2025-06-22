for _ in range(int(input())):
    n = int(input())
    s = input().strip()
    check = False
    cnt = [False]*26
    cnt[ord(s[0])-97] = True
    cnt[ord(s[n-1])-97] = True
    for i in range(1,n-1):
        if cnt[ord(s[i])-97]:
            check = True
            break
        cnt[ord(s[i])-97] = True
    print("Yes" if check else "No")