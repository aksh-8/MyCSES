n = int(input())

l = []
l.append(n)

while(n!=1):
    if(n%2 == 1):
        n = 3*n + 1
        l.append(n)
    else:
        n = n//2
        l.append(n)
    
for i in l:
    print(i, end=" ")