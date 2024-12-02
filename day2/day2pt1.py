with open("day2/input2.txt") as f:
    lines = f.readlines()

safe = 0
for line in lines:
  nums = [int(i) for i in line.split(" ")]
  
  if all(abs(i - j) <= 3 for i, j in zip(nums, nums[1:])):
    if all(i < j for i, j in zip(nums, nums[1:])):
      safe += 1
    elif all(i > j for i, j in zip(nums, nums[1:])):
      safe += 1


print(safe)