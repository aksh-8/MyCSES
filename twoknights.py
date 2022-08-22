n = int(input())

for i in range(1,n+1):
    #number of ways to place 2 knights on nxn board
    all_positions = ((i**2)*(i**2 - 1))/2            #knights identical assumed
    all_attacking_positions = 4*(i-1)*(i-2)
    all_non_attacking_positions = all_positions - all_attacking_positions
    print(int(all_non_attacking_positions))