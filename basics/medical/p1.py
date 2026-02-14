nums=list(map(int,input().split()))
nums.sort()
maxNum=nums[3]
print(maxNum-nums[0],maxNum-nums[1],maxNum-nums[2])