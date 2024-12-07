with open("day02/input2.txt") as f:
    lines = f.readlines()

safe = 0
for line in lines:
  nums = [int(i) for i in line.split(" ")]
  
  
  for n in range(len(nums)):
    
    changed = nums.copy()
    del changed[n]
    
    if all(abs(i - j) <= 3 for i, j in zip(changed, changed[1:])):
      if all(i < j for i, j in zip(changed, changed[1:])):
        safe += 1
        break
      elif all(i > j for i, j in zip(changed, changed[1:])):
        safe += 1
        break


print(safe)