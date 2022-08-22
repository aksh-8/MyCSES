from unicodedata import name


n = int(input())
l = list(map(int, input().split()))
s1 = 0
s2 = sum(l)
for i in range(1,n+1):
    s1 += i
print(s1-s2)


