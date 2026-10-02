s = input()
s2 = list(map(str, input().split()))
sa = set()
n = 0
for i in s:
    if i in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
        sa.add(i.lower())
        n += 1
p = {}
for i in sa:
    count = 0
    for j in s.lower:
        if i == j:
            count += 1
    p[i] = count

ans = 'a' * 100
for i in s2:
    flag = 1
    for char, count1 in p.items():
        if i.count(char) < count1:
            flag = 0
            break
    if flag == 1:
        if len(i) < len(ans):
            ans = i
print(ans)
