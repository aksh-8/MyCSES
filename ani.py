print("enter 10 values separated by space:")
l = list(map(int, input().split()))
t = tuple(l)

print("enter value to be searched:")
n = int(input())

l.pop(4)
t = tuple(l)

if n in t:
	print("the value exists in the tuple!")
	print("the position is: ", t.index(n))
else:
	print("the number doesn't exist in the tuple")