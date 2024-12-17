import re
with open("day17/input17_magic.txt") as f:
  registers, program = f.read().split("\n\n")

def combo(n):
  if 0 <= n <= 3:
    return n
  elif 4 <= n <= 6:
    return registers[n-4]
  elif n == 7:
    raise Exception("Combo operand 7 is reserved and will not appear in valid programs")
    
instruction_pointer = 0
program = [int(x) for x in re.findall(r"\d+", program)]
registers = [int(x) for x in re.findall(r"\d+", registers)] # A,B,C

while True:
  opcode = program[instruction_pointer]
  operand = program[instruction_pointer + 1]
  
  if opcode == 0:
    registers[0] = int(registers[0]/(2 ** combo(operand)))
  elif opcode == 1:
    registers[1] = registers[1] ^ operand
  elif opcode == 2:
    registers[1] = combo(operand) % 8
  elif opcode == 3:
    if registers[0] != 0:
      instruction_pointer = operand
      continue # do not incr by 2
  elif opcode == 4:
    registers[1] = registers[1] ^ registers[2]
  elif opcode == 5:
    print(combo(operand) % 8, end=",")
  elif opcode == 6:
    registers[1] = int(registers[0]/(2 ** combo(operand)))
  elif opcode == 7:
    registers[2] = int(registers[0]/(2 ** combo(operand)))
  
  instruction_pointer += 2
  if instruction_pointer >= len(program):
    break