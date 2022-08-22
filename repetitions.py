s = input()

m = 1
cnt = 1
l = []
for i in range(1, len(s)):
    if s[i]==s[i-1]:
        m += 1
    else:
        #l.append(m)
        m = 1
    if m>cnt:
        cnt = m

print(cnt)