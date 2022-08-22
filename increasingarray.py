n = int(input())
x_arr = list(map(int, input().split()))
moves = 0

for i in range(1,len(x_arr)):
    #print(x_arr[i])
    if x_arr[i-1] > x_arr[i]:
        diff = x_arr[i-1] - x_arr[i]
        moves = moves + abs(diff)
        x_arr[i] += abs(diff)
    else:
        moves = moves + 0
print(moves)