n = int(input())
nums = list(map(int, input().split()))
length = 1
nums.sort()
for i in range(1, n):
    if nums[i] != nums[i-1]:
        length += 1
print(length)