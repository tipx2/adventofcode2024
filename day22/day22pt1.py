with open("day22/input22.txt") as f:
  lines = [int(x.strip()) for x in f.readlines()]

def prune(secret_number):
  return secret_number % 16777216

def mix(num, secret_number):
  return num ^ secret_number


def calc(secret_number):
  for _ in range(2000):
    secret_number = mix(secret_number * 64, secret_number)
    secret_number = prune(secret_number)
    
    secret_number = mix(secret_number //32, secret_number)
    secret_number = prune(secret_number)
    
    secret_number = mix(secret_number * 2048, secret_number)
    secret_number = prune(secret_number)
    
  return secret_number

total = 0
for line in lines:
  total += calc(line)

print(total)