string = input().lower()
vowels = ('a','e','i','o','u')
i = 0
while i < len(string):
    x = string[i]
    if x in vowels:
        string = string[:i]+string[i+1:]
    else:
        string = string[:i]+'.'+string[i:]
        i += 2

print(string)